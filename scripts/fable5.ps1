# Fable 5 Offline Agent launcher — Windows PowerShell
# Usage:  .\scripts\fable5.ps1
#         .\scripts\fable5.ps1 --doctor
#         .\scripts\fable5.ps1 --loop "your goal"
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

function Find-Python {
    if ($env:FABLE5_PYTHON -and (Test-Path $env:FABLE5_PYTHON)) {
        return @{ Exe = $env:FABLE5_PYTHON; Args = @() }
    }
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return @{ Exe = "py"; Args = @("-3") }
    }
    foreach ($name in @("python", "python3")) {
        $cmd = Get-Command $name -ErrorAction SilentlyContinue
        if ($cmd) { return @{ Exe = $cmd.Source; Args = @() } }
    }
    throw "Python 3 not found. Install from https://www.python.org/downloads/ and enable PATH."
}

$Py = Find-Python
& $Py.Exe @($Py.Args) -c "import openai" 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing dependencies..."
    & $Py.Exe @($Py.Args) -m pip install -r (Join-Path $Root "requirements.txt")
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

& $Py.Exe @($Py.Args) (Join-Path $Root "fable5_offline_agent.py") @args
exit $LASTEXITCODE
