@echo off
REM Windows Script - Instagram Followers Checker

echo ======================================================================
echo Instagram Followers Checker - Windows
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo.
    echo Install Python from: https://www.python.org/downloads/
    echo IMPORTANT: Check the "Add Python to PATH" box during installation!
    echo.
    pause
    exit /b 1
)

echo Python detected: 
python --version
echo.

REM Check if instaloader is installed
python -c "import instaloader" >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] The 'instaloader' package is not installed!
    echo Installing automatically...
    echo.
    pip install instaloader
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Could not install instaloader!
        echo Try manually running: pip install instaloader
        echo.
        pause
        exit /b 1
    )
    echo.
    echo [OK] instaloader installed successfully!
    echo.
)

REM Run the script
echo Starting script...
echo.
python instagram_followers_checker.py

echo.
echo ======================================================================
echo Script finished!
echo ======================================================================
pause
