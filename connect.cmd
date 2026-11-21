@echo off
title NATHAN FELIX LIVE BRIDGE - TERMINAL EDITION
color 0E

echo ===============================================================================
echo               NATHAN FELIX LIVE BRIDGE - TERMINAL EDITION
echo                   Created by Nathan Felix - v3.0
echo ===============================================================================
echo.
echo [!] PENTING: Pastikan file connect.cmd dan connect.py ini sudah dipindahkan
echo     KE LUAR folder felix_bridge (ke root folder proyek Anda)!
echo ===============================================================================
echo.

:: Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan di laptop ini!
    echo Harap install Python terlebih dahulu dan pastikan dicentang "Add Python to PATH".
    pause
    exit /b
)

:: Check if paramiko is installed
python -c "import paramiko" >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Menginstall library Paramiko (SSH/SFTP Client)...
    pip install paramiko
    echo.
)

:: Run the terminal application
python connect.py %*
