# -*- coding:utf-8 -*-
"""

"""
# 导入包和模块
from PyQt5.Qt import *  # 常用的类


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowTitle")
        self.resize(500, 500)
        self.setup_ui()  # ui的设置

    def setup_ui(self):
        label = QLabel(self)
        label.setText("tettt")


if __name__ == '__main__':
    import sys  #

    app = QApplication(sys.argv)
    window = Window()
    # 显示窗口控件
    window.show()
    # 让整个程序无限循环，监测所有事件
    sys.exit(app.exec_())
