@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo No local virtual environment was found.
    echo Creating .venv and installing dependencies...
    echo.

    py -3 -m venv .venv >nul 2>&1
    if errorlevel 1 (
        python -m venv .venv >nul 2>&1
    )

    if not exist ".venv\Scripts\python.exe" (
        echo Python could not be found automatically.
        echo Please install Python 3.11+ and run this file again.
        pause
        exit /b 1
    )

    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Dependency installation failed.
        pause
        exit /b 1
    )
)

echo Starting PromoCatch on http://127.0.0.1:8010
echo Keep this window open while you use the app.
echo.

".venv\Scripts\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8010

echo.
echo PromoCatch has stopped.
pause
