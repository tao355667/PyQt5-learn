# -*- coding:utf-8 -*-
"""..."""
# 0.导入包和模块
from PyQt5.Qt import *  # 常用的类
import sys  #

# 1.创建一个应用程序对象
# 别人通过命令行启动这个程序时,可设定一种功能sys.argv (接收命令行传递的参数,执行不同的业务逻辑)
app = QApplication(sys.argv)
print(app.arguments())
print(qApp.arguments())
# 2.控件操作
# 创建窗口（控件），设置控件，事件，信号处理
# 2.1 创建控件
# 系统会自动给窗口一些装饰（标题栏），窗口控件具备一定的特性（设置标题，图标）
# window = QPushButton()
# window = QLabel()
window = QWidget()
# 2.2 设置控件
# window.setText("hello pyqt")
window.setWindowTitle("这是window Title")
# 控件可作为容器，承载其他控件
# label = QLabel()
label = QLabel(window)
label.setText("label.setText")
label.setWindowTitle("xxxxxxxx")# 若label无父控件，则此句生效
label.move(100,100)
label.show()
# 2.3 显示控件
# 控件没有父控件时，默认不会被显示
# 父控件显示，则子控件显示
window.show()
# 3.让整个程序无限循环，监测所有事件
# app.exec_()
# 4.退出码，0代表正确
sys.exit(app.exec_())
