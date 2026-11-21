@echo off
title NATHAN FELIX LIVE BRIDGE - CEK & INSTALL LIBRARY
color 0B

echo ===============================================================================
echo         NATHAN FELIX LIVE BRIDGE - PEMERIKSA & PEMASANG LIBRARY OTOMATIS
echo                      Created by Nathan Felix - v3.0
echo ===============================================================================
echo.
echo [!] Memeriksa kelengkapan library Python (Paramiko, CustomTkinter, Pillow)...
echo.

:: Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan di laptop ini!
    echo Harap install Python terlebih dahulu dan pastikan dicentang "Add Python to PATH".
    pause
    exit /b
)

:: Run the Python dependency checker & installer
python "%~dp0check_requirements.py"
