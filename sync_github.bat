@echo off
cd /d C:\Users\rafae\OneDrive\BeeCrowd-codes

:: Atualiza o repositório local com as mudanças do GitHub
git fetch origin main
for /f %%i in ('git rev-parse HEAD') do set LOCAL=%%i
for /f %%i in ('git rev-parse origin/main') do set REMOTE=%%i

if "%LOCAL%" NEQ "%REMOTE%" (
    echo 🔄 Alterações detectadas no GitHub! Atualizando...
    git pull origin main
) else (
    echo ✅ Nenhuma alteração nova no GitHub.
)
