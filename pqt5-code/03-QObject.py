# -*- coding:utf-8 -*-
"""

"""
# 导入包和模块
from PyQt5.Qt import *  # PyQt5常用的类


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject_test1()  # QObject继承结构测试
        self.QObject_test2()  # QObject API测试,qss
        self.QObject_test3()  # QObject 对象的父子关系

    def QObject_test1(self):  # QObject继承结构测试
        mros = QObject.mro()
        for mro in mros:
            print(mro)
        pass

    def QObject_test2(self):  # QObject API测试
        # ********测试API************开始
        # obj = QObject()
        # obj.setObjectName('notice')
        # print(obj.objectName())
        # obj.setProperty('notice_level', 'error')
        # obj.setProperty('notice_level2', 'waring')
        # print(obj.property('notice_level'))
        # print(obj.property('notice_level2'))
        #
        # print(obj.dynamicPropertyNames())
        # ********测试API*************结束

        # *******案例演示**************开始
        with open('QObject.qss', 'r') as f:
            qApp.setStyleSheet(f.read())
        label = QLabel(self)
        label.setText('label.setText!')
        label.setObjectName('notice')

        label2 = QLabel(self)
        label2.setText('一种自信')
        label2.move(0, 20)
        # label.setStyleSheet('font-size:20px;color:red;')
        # *******案例演示**************结束
        pass

    def QObject_test3(self):  # QObject 对象的父子关系
        # ********测试API*************开始
        # obj0 = QObject()
        # obj1 = QObject()
        # obj2 = QObject()
        # obj3 = QObject()
        # obj4 = QObject()
        # obj5 = QObject()
        # obj2.setObjectName("2")
        # obj3.setObjectName("3")
        # print("obj0", obj0)
        # print("obj1", obj1)
        # print("obj2", obj2)
        # print("obj3", obj3)
        # print("obj4", obj4)
        # print("obj5", obj5)
        # obj1.setParent(obj0)
        # obj2.setParent(obj0)
        # obj3.setParent(obj1)
        # obj4.setParent(obj2)
        # obj5.setParent(obj2)
        # # label = QLabel()
        # # label.setParent(obj0)#不能有这样一个父子关系
        # print(obj4.parent())
        # print(obj0.findChildren(QObject, "2"))
        # print(obj0.findChildren(QObject, "3"))  # 递归查找
        # ********测试API*************结束
        # ********内存管理机制*************开始
        obj1 = QObject()  # 父类对象被销毁时，子类对象也将被销毁
        self.obj1 = obj1
        obj2 = QObject()
        obj2.setParent(obj1)
        # 监听obj2对象被释放
        obj2.destroyed.connect(lambda: print("obj2对象被释放了"))
        del self, obj1
        # ********内存管理机制*************结束
        pass


if __name__ == '__main__':
    import sys  #

    app = QApplication(sys.argv)
    window = Window()
    # 显示窗口控件
    window.show()
    # ********对象父子*************开始
    # win1 = QWidget()
    # win1.setStyleSheet("background-color:red;")
    # win1.show()
    # win2 = QWidget()
    # win2.setStyleSheet("background-color:green;")
    # win2.setParent(win1)
    # win2.resize(50, 50)
    # win2.show()
    # ********对象父子*************结束

    # 让整个程序无限循环，监测所有事件
    sys.exit(app.exec_())
