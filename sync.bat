@echo off
cd /d C:\Users\rafae\OneDrive\BeeCrowd-codes

:: ==========================
:: 1️⃣ Puxa mudanças do repositório remoto antes de qualquer coisa
:: ==========================
echo 🔄 Verificando atualizações remotas...
git fetch origin main
for /f %%i in ('git rev-parse HEAD') do set LOCAL=%%i
for /f %%i in ('git rev-parse origin/main') do set REMOTE=%%i

:: Se houver mudanças remotas, faz o pull antes de qualquer coisa
if "%LOCAL%" NEQ "%REMOTE%" (
    echo 🚀 Atualizando repositório local com mudanças do GitHub...
    git pull --rebase origin main
    echo ✅ Atualização concluída.
)

:: ==========================
:: 2️⃣ Verifica se há mudanças locais (arquivos criados, modificados ou deletados)
:: ==========================
echo 🔍 Verificando mudanças locais...
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
    echo 📂 Novos arquivos detectados! Adicionando ao repositório...
    git add .
    git commit -m "Auto-sync: novos arquivos adicionados"
    git push origin main
    echo ✅ Novos arquivos sincronizados!
    exit /b 0
)

if %MODIFIED% neq 0 (
    echo ✏️ Arquivos modificados detectados! Salvando mudanças...
    git add .
    git commit -m "Auto-sync: alterações em arquivos existentes"
    git push origin main
    echo ✅ Arquivos modificados sincronizados!
    exit /b 0
)

if %DELETED% neq 1 (
    echo 🗑️ Arquivos deletados detectados! Atualizando repositório...
    git add .
    git commit -m "Auto-sync: arquivos deletados"
    git push origin main
    echo ✅ Exclusões sincronizadas!
    exit /b 0
)

:: ==========================
:: 4️⃣ Se não houver mudanças, sai silenciosamente
:: ==========================
echo ✅ Nenhuma alteração detectada. Nada a fazer.
exit /b 0
