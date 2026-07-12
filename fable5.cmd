@echo off
REM Fable 5 Offline Agent launcher — Windows (cmd.exe)
setlocal EnableExtensions
cd /d "%~dp0"

set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

set "PY="
if defined FABLE5_PYTHON if exist "%FABLE5_PYTHON%" set "PY=%FABLE5_PYTHON%"
if not defined PY where py >nul 2>&1 && set "PY=py -3"
if not defined PY where python >nul 2>&1 && set "PY=python"
if not defined PY where python3 >nul 2>&1 && set "PY=python3"
if not defined PY (
  echo error: Python 3 not found. Install from https://www.python.org/downloads/
  echo Enable "Add python.exe to PATH" during setup.
  exit /b 1
)

%PY% -c "import openai" >nul 2>&1
if errorlevel 1 (
  echo Installing dependencies...
  %PY% -m pip install -r "%~dp0requirements.txt"
  if errorlevel 1 exit /b 1
)

%PY% "%~dp0fable5_offline_agent.py" %*
exit /b %ERRORLEVEL%
