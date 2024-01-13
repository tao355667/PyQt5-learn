# -*- coding:utf-8 -*-
"""

"""
# 0.导入包和模块
from PyQt5.Qt import *  # 常用的类
import sys  #

from Menu import Window


# 1.创建一个应用程序对象
app = QApplication(sys.argv)
# 2.控件操作
# 创建窗口（控件），设置控件，事件，信号处理
# 2.1 创建窗口控件
window = Window()
# 2.2 设置窗口控件

# 新控件

# 显示窗口控件
window.show()
# 3.让整个程序无限循环，监测所有事件
sys.exit(app.exec_())
