#!/usr/bin/env bash
# Install Fable 5 Offline Agent deps — macOS / Linux
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "=== Fable 5 install (Unix) ==="
echo "OS: $(uname -s) $(uname -m)"

if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "Python 3.10+ required."
  exit 1
fi

echo "Python: $($PY --version)"
"$PY" -m pip install --upgrade pip
"$PY" -m pip install -r "$ROOT/requirements.txt"

chmod +x "$ROOT/fable5" "$ROOT/scripts/fable5.sh" "$ROOT/scripts/install.sh" 2>/dev/null || true

if command -v ollama >/dev/null 2>&1; then
  echo "Ollama: $(ollama --version 2>/dev/null || echo found)"
  echo "Pull a model if needed: ollama pull qwen2.5:7b"
else
  echo "Ollama not on PATH."
  echo "  macOS:  brew install ollama   or https://ollama.com/download"
  echo "  Linux:  curl -fsSL https://ollama.com/install.sh | sh"
fi

echo ""
"$PY" "$ROOT/fable5_offline_agent.py" --doctor || true
echo ""
echo "Run:  ./fable5"
echo "  or: python3 fable5_offline_agent.py"
