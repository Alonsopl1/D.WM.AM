@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Primero ejecuta iniciar_backend_windows.bat
  pause
  exit /b 1
)
echo Debes tener otra ventana con el backend ejecutandose.
".venv\Scripts\python.exe" -m pytest -q tests
pause
