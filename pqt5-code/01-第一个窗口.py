# -*- coding:utf-8 -*-
"""..."""
# 0.导入包和模块
from PyQt5.Qt import *  # 常用的类
import sys  #

# 1.创建一个应用程序对象
app = QApplication(sys.argv)
# 2.控件操作
# 创建窗口（控件），设置控件，事件，信号处理
window = QWidget()
window.setWindowTitle("one window!")  # 设置控件标题
window.resize(500, 500)  # 设置窗口大小
window.move(400, 200)  # 移动窗口
# 创建控件，设置控件
label = QLabel(window)
label.setText("Hello PYQT5~!")
label.move(200, 200)
# 打开窗口
window.show()
# 3.让整个程序无限循环，监测所有事件。退出码，0代表正确
sys.exit(app.exec_())
