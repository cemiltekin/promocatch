$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
    Write-Host "No local virtual environment was found."
    Write-Host "Creating .venv and installing dependencies..."
    Write-Host ""

    try {
        py -3 -m venv .venv
    }
    catch {
        python -m venv .venv
    }

    if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
        throw "Python could not be found automatically. Please install Python 3.11+ and run this script again."
    }

    & ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
}

Write-Host "Starting PromoCatch on http://127.0.0.1:8010"
Write-Host "Keep this window open while you use the app."
Write-Host ""

& ".\.venv\Scripts\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8010
