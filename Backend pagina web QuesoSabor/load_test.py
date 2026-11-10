@echo off
setlocal
chcp 65001 >NUL
cd /d "%~dp0"
echo ===========================================
echo    QUESO Y SABOR - EVALUACION 2 BACKEND
echo ===========================================
where py >NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
  echo No se encontro Python. Instala Python 3.11+ y marca "Add Python to PATH".
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  py -3 -m venv .venv
  if %ERRORLEVEL% NEQ 0 goto error
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 goto error
".venv\Scripts\python.exe" scripts\make_env.py
if %ERRORLEVEL% NEQ 0 goto error
echo.
echo API para probar: http://127.0.0.1:8000/api/v1/products?limit=100
echo Para detener: Ctrl+C
echo.
".venv\Scripts\python.exe" scripts\run_local.py
pause
exit /b 0
:error
echo.
echo Error de preparacion. Revisa el mensaje anterior.
pause
exit /b 1
