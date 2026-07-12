# Install Fable 5 Offline Agent deps — Windows PowerShell
# Usage:  powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root

Write-Host "=== Fable 5 install (Windows) ==="
Write-Host "OS: $([System.Environment]::OSVersion.VersionString)"

$Py = $null
$PyArgs = @()
if ($env:FABLE5_PYTHON -and (Test-Path $env:FABLE5_PYTHON)) {
    $Py = $env:FABLE5_PYTHON
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $Py = "py"
    $PyArgs = @("-3")
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $Py = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $Py = "python3"
} else {
    throw "Python 3.10+ required. https://www.python.org/downloads/ (check Add to PATH)"
}

Write-Host "Python: $(& $Py @PyArgs --version)"
& $Py @PyArgs -m pip install --upgrade pip
& $Py @PyArgs -m pip install -r (Join-Path $Root "requirements.txt")

if (Get-Command ollama -ErrorAction SilentlyContinue) {
    Write-Host "Ollama: found"
    Write-Host "Pull a model if needed: ollama pull qwen2.5:7b"
} else {
    Write-Host "Ollama not on PATH. Install: https://ollama.com/download"
}

Write-Host ""
& $Py @PyArgs (Join-Path $Root "fable5_offline_agent.py") --doctor
Write-Host ""
Write-Host "Run:  .\fable5.cmd"
Write-Host "  or: .\scripts\fable5.ps1"
Write-Host "  or: python fable5_offline_agent.py"
