@echo off
setlocal enabledelayedexpansion

rem Define the base port number
set base_port=1234

rem Loop to create 12 servers
for /l %%i in (1, 1, 12) do (
  set /a port=!base_port!+%%i
  start node main.js !port!
)

echo Servers are running.
pause
