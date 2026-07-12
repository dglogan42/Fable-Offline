#!/usr/bin/env bash
# Thin wrapper — same as ../fable5
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$ROOT/fable5" "$@"
