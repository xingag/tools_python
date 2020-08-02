@echo off  

title 循环运行Python代码

:: 5分钟执行一次，单位为s
set INTERVAL=300

:: 提前执行一次，把执行时间打印出来
echo 开始执行 - %time%
python C:/test.py 

:: 使用timeout进行倒计时
timeout %INTERVAL%

:: 新建一个任务
:Task  
echo 开始执行 - %time%
python C:/test.py 
timeout %INTERVAL%

:: 使用goto命令，开始跳转到上面的任务，开始执行
goto Task  