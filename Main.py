#!/usr/bin/python3
'''
Author By Lihongchi
Create Date from 2018/7/8
'''
# -*- coding: utf-8 -*-

import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow


#通过pyuic产生的py文件
from MainUI import Ui_MainWindow

#导入pyuid产生的py文件对应的信号事件函数
from MainUIConn import setBMIndexBtnConn,setGaiKuangBtnConn,setXXGKIndexColumnBtnConn,\
    setXXGKStaticInfoBtnConn,setBMGGGSBtnConn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()

    #设置UI界面
    ui.setupUi(MainWindow)
    #设置子界面是否打开标志列表
    SubWinList = {'BMIndex':0,'GaiKuang':0,'XXGKIndexColumn':0,'XXGKStaticInfo':0,'BMGGGS':0}

    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

    # 设置UI组件信号
    setBMIndexBtnConn(father_path,SubWinList, ui.actionBMGKIndex, ui, MainWindow)
    setGaiKuangBtnConn(father_path, SubWinList, ui.actionBMGaiKuang, ui, MainWindow)
    setXXGKIndexColumnBtnConn(father_path, SubWinList, ui.actionXXGKIndexColumn, ui, MainWindow)
    setXXGKStaticInfoBtnConn(father_path, SubWinList, ui.actionXXGKStaticInfo, ui, MainWindow)
    setBMGGGSBtnConn(father_path, SubWinList, ui.actionBMGGGS, ui, MainWindow)

    #显示主窗口
    MainWindow.resize(1200, 750)
    MainWindow.show()


    sys.exit(app.exec_())
