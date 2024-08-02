@echo off
python monitor_windows.py
powershell -ExecutionPolicy Bypass -File monitor.ps1
