@echo off
title NATHAN FELIX LIVE BRIDGE - AUTOMATIC SETUP
color 0A

echo ===============================================================================
echo            NATHAN FELIX LIVE BRIDGE - AUTOMATIC LAUNCHER SETUP
echo                    Created by Nathan Felix - v3.0
echo ===============================================================================
echo.
echo [!] Installing launcher bridge files to your project root...
echo.

:: %~dp0 is current directory (felix_bridge\)
:: %~dp0.. is parent directory (project root)

copy /Y "%~dp0gui.py" "%~dp0..\gui.py" >nul
copy /Y "%~dp0gui.cmd" "%~dp0..\gui.cmd" >nul
copy /Y "%~dp0connect.py" "%~dp0..\connect.py" >nul
copy /Y "%~dp0connect.cmd" "%~dp0..\connect.cmd" >nul

echo [✔ SUCCESS!!] All 4 launcher files have been automatically deployed outside!
echo.
echo Deployment Path: %~dp0..
echo.
echo You can now go back to your main project folder and double-click
echo 'gui.cmd' or 'connect.cmd' to start real-time live coding!
echo.
echo ===============================================================================
pause
