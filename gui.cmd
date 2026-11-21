@echo off
title NATHAN FELIX LIVE BRIDGE - ENTERPRISE GUI
color 0E

echo ===============================================================================
echo                NATHAN FELIX LIVE BRIDGE - ENTERPRISE GUI
echo                   Created by Nathan Felix - v3.0
echo ===============================================================================
echo.
echo [!] PENTING: Pastikan file gui.cmd dan gui.py ini sudah dipindahkan
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

:: Check if required GUI libraries are installed
python -c "import customtkinter, PIL, paramiko" >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Memeriksa dan menginstall library GUI (CustomTkinter, Pillow, Paramiko)...
    pip install customtkinter pillow paramiko
    echo.
)

:: Launch the GUI application
python gui.py %*
