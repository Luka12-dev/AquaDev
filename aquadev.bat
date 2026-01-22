@echo off
REM ============================================================
REM AquaDev - AI Development Agent
REM 100% Local | 100% Private | Open Source
REM ============================================================
REM GitHub: https://github.com/Luka12-dev/AquaDev
REM YouTube: https://www.youtube.com/@LukaCyber-s4b7o
REM ============================================================

REM Get the directory where this batch file is located
set "AQUADEV_DIR=%~dp0"

REM Run aquadev.py from its location, but stay in current working directory
python "%AQUADEV_DIR%aquadev.py" %*
