# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import QMdiSubWindow,QMessageBox
from SubWinUI.BMGGGS.BMGGGSUI import Ui_BMGGGSForm

from RuiJinModule.BMGGGS.ScanProfile import ScanBMGGGS,ViewReport

class BMGGGSForm(QMdiSubWindow):
    """QMdiSubWindow，实现一些功能"""
    def __init__(self,SubWinList,parent,MainWindow):
        # super(BMIndexForm,self) 首先找到 BMIndexForm 的父类（就是类 QMdiSubWindow），
        # 然后把类的对象 BMIndexForm 转换为类 QMdiSubWindow 的对象
        super(BMGGGSForm, self).__init__()
        self.SubWinList = SubWinList

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现QMdiSubWindow窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,'关闭窗口',"是否要关闭此窗口？",QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.SubWinList['BMGGGS'] = 0
            #print(self.SubWinList['DongTai'])
            event.accept()
        else:
            event.ignore()
def getBMGGGSForm(father_path,SubWinList,UIBtn,UI,MainWindow):
    if (SubWinList['BMGGGS'] == 0):
        MyForm = BMGGGSForm(SubWinList,UI.mdiArea,MainWindow)
        #MyWin.setWindowTitle("mdisubwindow")
        #MyWin.setGeometry(QtCore.QRect(0, 0, 800, 600))

        MyFormUI = Ui_BMGGGSForm()
        # 设置UI界面
        MyFormUI.setupUi(MyForm)

        UI.mdiArea.addSubWindow(MyForm)
        SubWinList['BMGGGS'] = 1

        # 设置UI组件信号
        MyFormUI.DoScanProfileBtn.clicked.connect(lambda: ScanBMGGGS(MyFormUI.DoScanProfileBtn, MyFormUI, MyForm))
        MyFormUI.ViewReportBtn.clicked.connect(lambda: ViewReport(MyFormUI.DoScanProfileBtn, MyFormUI, MyForm))

        MyFormUI.ProfileLineEdit.setText(father_path+"\\RuiJinModule\\BMGGGS\Profile\\bmgkxx_bmgggs.profile")

        MyForm.show()