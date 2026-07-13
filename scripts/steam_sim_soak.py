#!/usr/bin/env python3
"""
One-shot SIM soak: measure Ollama latency with/without a Steam game.

  python scripts/steam_sim_soak.py
  python scripts/steam_sim_soak.py --appid 24780 --skip-relaunch

Does not automate gameplay. Stops/starts the known process for A/B only.
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent

KNOWN_PROCESS = {
    "24780": "SimCity 4",
}

BASE = "http://127.0.0.1:11434"
DEFAULT_MODEL = "qwen2.5:7b"
PROMPT = "Reply with exactly one word: pong"
N = 3


def process_snapshot(names: list[str]) -> list[dict]:
    rows: list[dict] = []
    for name in names:
        try:
            # Avoid nested PowerShell — use tasklist / WMIC-style via Get-Process is fine in one call
            ps = (
                f"Get-Process -Name '{name}' -ErrorAction SilentlyContinue | "
                "ForEach-Object { "
                "[PSCustomObject]@{ Name=$_.Name; Id=$_.Id; "
                "WS_MB=[math]::Round($_.WorkingSet64/1MB,1); "
                "CPU_s=[math]::Round($_.CPU,1) } } | ConvertTo-Json -Compress"
            )
            r = subprocess.run(
                ["powershell", "-NoProfile", "-Command", ps],
                capture_output=True,
                text=True,
                timeout=30,
            )
            raw = (r.stdout or "").strip()
            if not raw:
                continue
            data = json.loads(raw)
            if isinstance(data, dict):
                rows.append(data)
            else:
                rows.extend(data)
        except Exception as e:
            rows.append({"Name": name, "error": str(e)})
    return rows


def one_generate(
    model: str,
    prompt: str = PROMPT,
    num_predict: int = 16,
) -> dict:
    body = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": True,
            "options": {"num_predict": num_predict, "temperature": 0},
        }
    ).encode()
    req = urllib.request.Request(
        BASE + "/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.perf_counter()
    ttft = None
    text: list[str] = []
    eval_count = None
    eval_duration = None
    with urllib.request.urlopen(req, timeout=180) as resp:
        for raw in resp:
            line = raw.decode("utf-8", errors="replace").strip()
            if not line:
                continue
            obj = json.loads(line)
            piece = obj.get("response") or ""
            if piece and ttft is None:
                ttft = time.perf_counter() - t0
            text.append(piece)
            if obj.get("done"):
                eval_count = obj.get("eval_count")
                eval_duration = obj.get("eval_duration")
    total = time.perf_counter() - t0
    tok_s = None
    if eval_count and eval_duration and eval_duration > 0:
        tok_s = eval_count / (eval_duration / 1e9)
    return {
        "ttft_s": ttft,
        "total_s": total,
        "tokens": eval_count,
        "tok_s": tok_s,
        "text": "".join(text).strip()[:80],
    }


def run_phase(label: str, watch: list[str], model: str) -> dict | None:
    print(f"\n=== PHASE: {label} ===")
    snap = process_snapshot(watch)
    print("Processes:")
    if snap:
        for row in snap:
            print(" ", row)
    else:
        print("  (none of watched processes running)")
    try:
        one_generate(model)  # warmup discard
    except Exception as e:
        print("WARMUP FAIL:", e)
        return None
    results = []
    for i in range(N):
        try:
            r = one_generate(model)
            results.append(r)
            tps = f"{r['tok_s']:.1f}" if r["tok_s"] else "n/a"
            print(
                f"  run {i + 1}: ttft={r['ttft_s']:.3f}s total={r['total_s']:.3f}s "
                f"tokens={r['tokens']} tok/s={tps} text={r['text']!r}"
            )
        except Exception as e:
            print(f"  run {i + 1}: FAIL {e}")
    if not results:
        return None
    ttfts = [r["ttft_s"] for r in results if r["ttft_s"] is not None]
    totals = [r["total_s"] for r in results]
    toks = [r["tok_s"] for r in results if r["tok_s"]]
    summary = {
        "label": label,
        "ttft_mean": statistics.mean(ttfts) if ttfts else None,
        "ttft_min": min(ttfts) if ttfts else None,
        "total_mean": statistics.mean(totals),
        "total_min": min(totals),
        "tok_s_mean": statistics.mean(toks) if toks else None,
        "n": len(results),
        "processes": snap,
    }
    tps = f"{summary['tok_s_mean']:.1f}" if summary["tok_s_mean"] else "n/a"
    print(
        f"  SUMMARY {label}: ttft_mean={summary['ttft_mean']:.3f}s "
        f"total_mean={summary['total_mean']:.3f}s tok/s_mean={tps}"
    )
    return summary


def stop_process(name: str) -> None:
    print(f"\n=== Stopping process: {name} ===")
    subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            f"Get-Process -Name '{name}' -ErrorAction SilentlyContinue | Stop-Process",
        ],
        check=False,
    )
    time.sleep(4)


def launch_app(appid: str) -> None:
    print(f"\n=== Launching AppID {appid} ===")
    r = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "steam_launch.py"), appid],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    print(r.stdout or "")
    if r.stderr:
        print(r.stderr)
    time.sleep(8)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="SIM + Ollama latency soak")
    ap.add_argument("--appid", default="24780")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--skip-relaunch", action="store_true")
    ap.add_argument("--no-stop", action="store_true", help="Only measure under current load")
    args = ap.parse_args(argv)

    model = args.model
    appid = args.appid
    proc_name = KNOWN_PROCESS.get(appid, "SimCity 4")
    watch = [proc_name, "ollama"]

    print(f"Model: {model}")
    print(f"AppID: {appid}  process: {proc_name}")
    print(f"Ollama: {BASE}")

    # Ensure game running for load phase
    snap0 = process_snapshot([proc_name])
    if not snap0:
        launch_app(appid)
    else:
        print(f"\n{proc_name} already running — using as load phase")

    load = run_phase("WITH_SC4", watch, model)

    baseline = None
    if not args.no_stop:
        stop_process(proc_name)
        baseline = run_phase("NO_SC4", watch, model)
        if not args.skip_relaunch:
            launch_app(appid)
            print("After relaunch:")
            for row in process_snapshot(watch):
                print(" ", row)

    print("\n=== SOAK VERDICT ===")
    if load and baseline:
        d_ttft = load["ttft_mean"] - baseline["ttft_mean"]
        d_tot = load["total_mean"] - baseline["total_mean"]
        d_tok = None
        if load["tok_s_mean"] and baseline["tok_s_mean"]:
            d_tok = baseline["tok_s_mean"] - load["tok_s_mean"]
        print(
            f"Baseline (no SC4): ttft={baseline['ttft_mean']:.3f}s "
            f"total={baseline['total_mean']:.3f}s tok/s={baseline['tok_s_mean']:.1f}"
        )
        print(
            f"With SC4:          ttft={load['ttft_mean']:.3f}s "
            f"total={load['total_mean']:.3f}s tok/s={load['tok_s_mean']:.1f}"
        )
        tok_drop = f"{d_tok:+.1f}" if d_tok is not None else "n/a"
        print(f"Delta (load-base): ttft={d_ttft:+.3f}s total={d_tot:+.3f}s tok/s_drop={tok_drop}")
        if load["ttft_mean"] < 2.0 and load["tok_s_mean"] and load["tok_s_mean"] > 15:
            verdict = "usable under SC4 load"
        elif load["ttft_mean"] < 5.0:
            verdict = "degraded but usable for light chat"
        else:
            verdict = "heavily degraded / avoid heavy loops while SC4 runs"
        print(f"Verdict: {verdict}")
    elif load:
        print(
            f"With SC4 only: ttft={load['ttft_mean']:.3f}s "
            f"total={load['total_mean']:.3f}s tok/s={load['tok_s_mean']}"
        )
        print("Verdict: load-only sample (no baseline)")
    else:
        print("Incomplete metrics")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
