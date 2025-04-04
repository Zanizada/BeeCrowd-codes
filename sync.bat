@echo off
cd /d C:\Users\rafae\OneDrive\BeeCrowd-codes

:: Verifica se há arquivos novos ou modificados
git fetch origin main
for /f %%i in ('git rev-parse HEAD') do set LOCAL=%%i
for /f %%i in ('git rev-parse origin/main') do set REMOTE=%%i

:: Checa se há modificações no repositório
git status --porcelain | findstr /R "^\?\? ^ M" > nul
if %errorlevel% neq 0 (
    git pull origin main
    git add .
    git commit -m "Auto-sync: atualização automática"
    git push origin main
) else (
    exit /b 0
)
