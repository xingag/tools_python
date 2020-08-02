@echo off
:: 打开到当前目录下
cd /d "%~dp0"

:: 删除build文件夹
echo 开始删除

for /r /D %%i in (*build*) do rd /s /q "%%i"

echo 删除完成

pause