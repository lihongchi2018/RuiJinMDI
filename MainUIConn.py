# -*- coding: utf-8 -*-

from SubWinUI.BMIndex.BMIndexClass import getBMIndexForm
from SubWinUI.GaiKuang.GaiKuangClass import getGaiKuangForm
from SubWinUI.XXGKIndexColumn.XXGKIndexColumnClass import getXXGKIndexColumnForm
from SubWinUI.XXGKStaticInfo.XXGKStaticInfoClass import getXXGKStaticInfoForm
from SubWinUI.BMGGGS.BMGGGSClass import getBMGGGSForm

def setBMIndexBtnConn(father_path,SubWinList,UIBtn,UI,MainWindow):
    # 绑定按钮click
    UIBtn.triggered.connect(lambda: getBMIndexForm(father_path,SubWinList,UIBtn,UI,MainWindow))

def setGaiKuangBtnConn(father_path,SubWinList,UIBtn,UI,MainWindow):
    # 绑定按钮click
    UIBtn.triggered.connect(lambda: getGaiKuangForm(father_path,SubWinList,UIBtn,UI,MainWindow))

def setXXGKIndexColumnBtnConn(father_path,SubWinList,UIBtn,UI,MainWindow):
    # 绑定按钮click
    UIBtn.triggered.connect(lambda: getXXGKIndexColumnForm(father_path,SubWinList,UIBtn,UI,MainWindow))

def setXXGKStaticInfoBtnConn(father_path,SubWinList,UIBtn,UI,MainWindow):
    # 绑定按钮click
    UIBtn.triggered.connect(lambda: getXXGKStaticInfoForm(father_path, SubWinList, UIBtn, UI, MainWindow))

def setBMGGGSBtnConn(father_path,SubWinList,UIBtn,UI,MainWindow):
    # 绑定按钮click
    UIBtn.triggered.connect(lambda: getBMGGGSForm(father_path, SubWinList, UIBtn, UI, MainWindow))
