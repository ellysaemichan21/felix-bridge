@echo off
title NATHAN FELIX LIVE BRIDGE - AUTOMATIC SETUP
color 0A

echo ===============================================================================
echo            NATHAN FELIX LIVE BRIDGE - PEMASANGAN OTOMATIS
echo                    Created by Nathan Felix - v3.0
echo ===============================================================================
echo.
echo [!] Sedang memasang file launcher ke folder root proyek Anda...
echo.

:: %~dp0 adalah folder saat ini (felix_bridge\)
:: %~dp0.. adalah folder induk (root proyek tempat folder felix_bridge diletakkan)

copy /Y "%~dp0gui.py" "%~dp0..\gui.py" >nul
copy /Y "%~dp0gui.cmd" "%~dp0..\gui.cmd" >nul
copy /Y "%~dp0connect.py" "%~dp0..\connect.py" >nul
copy /Y "%~dp0connect.cmd" "%~dp0..\connect.cmd" >nul

echo [✔ BERHASIL!!] Ke-4 file launcher telah otomatis dipasang ke luar folder!
echo.
echo Lokasi Pemasangan: %~dp0..
echo.
echo Sekarang Anda bisa kembali ke folder utama proyek Anda dan langsung
echo mengklik ganda 'gui.cmd' atau 'connect.cmd' untuk memulai live coding!
echo.
echo ===============================================================================
pause
