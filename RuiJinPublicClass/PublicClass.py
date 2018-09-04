# -*- coding: utf-8 -*-

import os
from PyQt5.QtWidgets import QWidget,QMessageBox


class AlertMessage(QWidget):
    def __init__(self,MainWindow,MessageText):
        super(AlertMessage, self).__init__()
        self.initUi(MainWindow,MessageText)

    def initUi(self,MainWindow,MessageText):
        # print("InfoDialog")
        rect = MainWindow.geometry()
        # print("rect.left(), rect.top()-->",rect.left(), rect.top())
        # print("rect.width(), rect.height()-->",rect.width(), rect.height())
        self.move(rect.left() + 100, rect.top() + 100)
        QMessageBox.information(self, "提示标题",MessageText , QMessageBox.Yes)

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False