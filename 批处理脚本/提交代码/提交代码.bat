@echo off
title 提交代码
echo 提交代码，简化操作

:: 代码状态
:: https://www.jb51.net/article/188202.htm
git status

:: set：等待输入，赋值给变量msg
set /p commit_msg=代码提交注释：

:: 提交代码的4条命令
git add .
git commit -m %commit_msg%
git pull
git push

echo 提交成功
pause


