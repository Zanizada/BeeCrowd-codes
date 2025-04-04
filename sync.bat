@echo off
cd /d "C:\Users\rafae\OneDrive\BeeCrowd-codes"  REM Caminho do seu repositório local

echo Atualizando repositório...
git pull origin main

echo Adicionando novos arquivos...
git add .

echo Criando commit...
git commit -m "Atualização automática dos códigos"

echo Enviando para o GitHub...
git push origin main

echo Sincronização concluída!
pause
