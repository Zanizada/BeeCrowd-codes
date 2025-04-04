@echo off
cd /d C:\Users\rafae\OneDrive\BeeCrowd-codes

:: Verifica se há arquivos novos, modificados ou deletados
git fetch origin main
git ls-files --others --exclude-standard | findstr "." > nul
set NEWFILES=%errorlevel%

git diff --quiet --exit-code
set MODIFIED=%errorlevel%

git ls-files --deleted | findstr "." > nul
set DELETED=%errorlevel%

:: Se houver qualquer alteração (arquivos novos, modificados ou deletados), faz o commit e o push
if %NEWFILES% neq 1 (
    git add .
    git commit -m "Auto-sync: novos arquivos adicionados"
    git push origin main
    exit /b 0
)

if %MODIFIED% neq 0 (
    git add .
    git commit -m "Auto-sync: alterações em arquivos existentes"
    git push origin main
    exit /b 0
)

if %DELETED% neq 1 (
    git add .
    git commit -m "Auto-sync: arquivos deletados"
    git push origin main
    exit /b 0
)

:: Se não houver mudanças, sai sem abrir o prompt
exit /b 0
