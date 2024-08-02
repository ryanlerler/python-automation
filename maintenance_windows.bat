@echo off
echo Running maintenance tasks...
del /s /q %temp%\*
del /s /q C:\Windows\Temp\*
echo Maintenance tasks completed.
