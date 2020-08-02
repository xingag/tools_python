@echo off
:: 当前目录下的文件进行分类，放到不同的文件夹内
:: md 用于创建文件夹
:: %%~xi将%%i解开扩展名，也就是取%%i的扩展名部分 
for %%i in (*) do (md %%~xi 
move *%%~xi %%~xi)

pause