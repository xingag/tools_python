#include <GuiListView.au3>

; 注意：对于非标准控件，没法利用Autoit的拿到控件的属性

; 选中窗口
;$handle = WinGetHandle("一键升级","")
$handle = WinGetHandle("source","")

WinActivate($handle)

;全选
Send("^a")


;右键
MouseClick("right")

; 点击A，相当于选择[添加到压缩文件]
Send('A')


$handle = WinGetHandle("压缩文件名和参数","")
WinActivate($handle)

Sleep(1000)

; 压缩选中自解压文件
ControlClick("压缩文件名和参数","","Button9")


Sleep(1000)


;跳到高级Tab
Send("^{TAB}")

Sleep(1000)

;点击自解压选项
ControlClick("压缩文件名和参数","","Button11")

Sleep(1000)

;跳到设置Tab
Send("^{TAB}")

Sleep(1000)

;提取后运行的程序
ControlSetText("高级自解压选项","","Edit1","DGUpdata.exe")

Sleep(1000)

;等待退出
ControlClick("高级自解压选项","","Button2")

Sleep(1000)

;跳到模式Tab
Send("^{TAB}")

Sleep(1000)

;临时文件夹及隐藏
ControlClick("高级自解压选项","","Button2")

Sleep(1000)

ControlClick("高级自解压选项","","Button6")

Sleep(1000)


; 调到文本和图标Tab，执行3次Tab键
Send("^{TAB 3}")

Sleep(1000)

;点击浏览按钮
ControlClick("高级自解压选项","","Button4")

;选择文件 update.ico
ControlFocus("选择图标","","Edit1")


Sleep(1000)

ControlSetText("选择图标","","Edit1","update.ico")

Sleep(1000)

; 确定选择文件
ControlClick("选择图标","","Button1")

;调到许可Tab
Sleep(1000)
Send("^{TAB}")


;模拟点击回车键，执行压缩操作
Send("{ENTER}")

Send("^{TAB}")

Send("{ENTER}")

; 点击确定
; 注意：由于【确定按钮】的ClassNameNN经常会变化，没有办法用下面的方法执行
; ControlClick("高级自解压选项","","Button7")





