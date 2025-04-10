@echo off
cd /d C:\Users\rafae\OneDrive\BeeCrowd-codes

echo [%date% %time%] 🚀 Iniciando sincronização... >> sync_log.txt 2>&1

:: ==========================
:: 1️⃣ Puxa mudanças do repositório remoto antes de qualquer coisa
:: ==========================
echo 🔄 Verificando atualizações remotas... >> sync_log.txt 2>&1
git fetch origin main >> sync_log.txt 2>&1
for /f %%i in ('git rev-parse HEAD') do set LOCAL=%%i
for /f %%i in ('git rev-parse origin/main') do set REMOTE=%%i

if "%LOCAL%" NEQ "%REMOTE%" (
    echo 🚀 Atualizando repositório local com mudanças do GitHub... >> sync_log.txt 2>&1
    git pull --rebase origin main >> sync_log.txt 2>&1
    echo ✅ Atualização concluída. >> sync_log.txt 2>&1
)

:: ==========================
:: 2️⃣ Verifica se há mudanças locais (arquivos criados, modificados ou deletados)
:: ==========================
echo 🔍 Verificando mudanças locais... >> sync_log.txt 2>&1
git ls-files --others --exclude-standard | findstr "." > nul
set NEWFILES=%errorlevel%

git diff --quiet --exit-code
set MODIFIED=%errorlevel%

git ls-files --deleted | findstr "." > nul
set DELETED=%errorlevel%

:: ==========================
:: 3️⃣ Se houver mudanças locais, adiciona, commita e faz push
:: ==========================
if %NEWFILES% neq 1 (
    echo 📂 Novos arquivos detectados! Adicionando ao repositório... >> sync_log.txt 2>&1
    git add . >> sync_log.txt 2>&1
    git commit -m "New item listed in local repository" >> sync_log.txt 2>&1
    git push origin main >> sync_log.txt 2>&1
    echo ✅ Novos arquivos sincronizados! >> sync_log.txt 2>&1
    echo [%date% %time%] ✅ Fim da sincronização. >> sync_log.txt 2>&1
    exit /b 0
)

if %MODIFIED% neq 0 (
    echo ✏️ Arquivos modificados detectados! Salvando mudanças... >> sync_log.txt 2>&1
    git add . >> sync_log.txt 2>&1
    git commit -m "File modified in local repository" >> sync_log.txt 2>&1
    git push origin main >> sync_log.txt 2>&1
    echo ✅ Arquivos modificados sincronizados! >> sync_log.txt 2>&1
    echo [%date% %time%] ✅ Fim da sincronização. >> sync_log.txt 2>&1
    exit /b 0
)

if %DELETED% neq 1 (
    echo 🗑️ Arquivos deletados detectados! Atualizando repositório... >> sync_log.txt 2>&1
    git add . >> sync_log.txt 2>&1
    git commit -m "File deleted in local repository" >> sync_log.txt 2>&1
    git push origin main >> sync_log.txt 2>&1
    echo ✅ Exclusões sincronizadas! >> sync_log.txt 2>&1
    echo [%date% %time%] ✅ Fim da sincronização. >> sync_log.txt 2>&1
    exit /b 0
)

:: ==========================
:: 4️⃣ Se não houver mudanças, sai silenciosamente
:: ==========================
echo ✅ Nenhuma alteração detectada. Nada a fazer. >> sync_log.txt 2>&1
echo [%date% %time%] ✅ Fim da sincronização. >> sync_log.txt 2>&1
exit /b 0
