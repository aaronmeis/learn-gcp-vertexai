@echo off
REM Quick activation script for Windows Command Prompt
REM Run this script to activate the virtual environment and set up environment variables
REM Note: This script should be CALLed, not run directly, to preserve environment variables
setlocal enabledelayedexpansion

echo Activating virtual environment...

REM Activate virtual environment
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
) else (
    echo [ERROR] Virtual environment not found. Run setup-windows.bat first.
    pause
    exit /b 1
)

REM Load environment variables from .env file if it exists
if exist .env (
    echo.
    echo Loading environment variables from .env...
    for /f "usebackq tokens=1,* delims==" %%a in (".env") do (
        REM %%a = key, %%b = value
        REM Skip empty keys and keys starting with #
        if not "%%a"=="" (
            REM Check if key starts with # (comment)
            echo %%a | findstr /R "^#" >nul
            if errorlevel 1 (
                REM Not a comment line, process it
                REM Trim spaces from key
                for /f "tokens=*" %%k in ("%%a") do set "envkey=%%k"
                REM Trim spaces from value
                if not "%%b"=="" (
                    for /f "tokens=*" %%v in ("%%b") do set "envval=%%v"
                ) else (
                    set "envval="
                )
                REM Skip if value is placeholder
                if not "!envval!"=="your-project-id" (
                    REM Set environment variable (will persist in CMD session)
                    set "!envkey!=!envval!"
                    echo   [OK] !envkey! = !envval!
                )
            )
        )
    )
    echo [OK] Environment variables loaded
) else (
    echo.
    echo [WARNING] .env file not found. Using system environment variables.
)

REM Check if project ID is set
if "%GOOGLE_CLOUD_PROJECT%"=="" (
    echo.
    echo [WARNING] GOOGLE_CLOUD_PROJECT not set. Set it with:
    echo    set GOOGLE_CLOUD_PROJECT=your-project-id
) else (
    echo.
    echo [OK] Project ID: %GOOGLE_CLOUD_PROJECT%
)

echo.
echo [SUCCESS] Environment ready!
echo You can now run:
echo   python week-01-gemini-fundamentals\demos\hello_world_agent_local.py

