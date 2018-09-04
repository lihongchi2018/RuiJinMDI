# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMIndexUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BMIndexForm(object):
    def setupUi(self, BMIndexForm):
        BMIndexForm.setObjectName("BMIndexForm")
        BMIndexForm.resize(1006, 524)
        self.ProfileLineEdit = QtWidgets.QLineEdit(BMIndexForm)
        self.ProfileLineEdit.setGeometry(QtCore.QRect(100, 50, 731, 31))
        self.ProfileLineEdit.setObjectName("ProfileLineEdit")
        self.ScanTextEdit = QtWidgets.QTextEdit(BMIndexForm)
        self.ScanTextEdit.setGeometry(QtCore.QRect(20, 110, 961, 311))
        self.ScanTextEdit.setObjectName("ScanTextEdit")
        self.JCBGLineEdit = QtWidgets.QLineEdit(BMIndexForm)
        self.JCBGLineEdit.setGeometry(QtCore.QRect(90, 440, 751, 31))
        self.JCBGLineEdit.setObjectName("JCBGLineEdit")
        self.DoScanProfileBtn = QtWidgets.QPushButton(BMIndexForm)
        self.DoScanProfileBtn.setGeometry(QtCore.QRect(850, 40, 131, 41))
        self.DoScanProfileBtn.setObjectName("DoScanProfileBtn")
        self.ViewReportBtn = QtWidgets.QPushButton(BMIndexForm)
        self.ViewReportBtn.setGeometry(QtCore.QRect(854, 432, 131, 41))
        self.ViewReportBtn.setObjectName("ViewReportBtn")
        self.ReportLbl = QtWidgets.QLabel(BMIndexForm)
        self.ReportLbl.setGeometry(QtCore.QRect(20, 440, 71, 31))
        self.ReportLbl.setObjectName("ReportLbl")
        self.ProfileLbl = QtWidgets.QLabel(BMIndexForm)
        self.ProfileLbl.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.ProfileLbl.setObjectName("ProfileLbl")
        self.TipInfoLbl = QtWidgets.QLabel(BMIndexForm)
        self.TipInfoLbl.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.TipInfoLbl.setObjectName("TipInfoLbl")

        self.retranslateUi(BMIndexForm)
        QtCore.QMetaObject.connectSlotsByName(BMIndexForm)

    def retranslateUi(self, BMIndexForm):
        _translate = QtCore.QCoreApplication.translate
        BMIndexForm.setWindowTitle(_translate("BMIndexForm", "部门首页"))
        self.DoScanProfileBtn.setText(_translate("BMIndexForm", "执行配置文件检测"))
        self.ViewReportBtn.setText(_translate("BMIndexForm", "查看检测报告"))
        self.ReportLbl.setText(_translate("BMIndexForm", "检测报告："))
        self.ProfileLbl.setText(_translate("BMIndexForm", "配置文件："))
        self.TipInfoLbl.setText(_translate("BMIndexForm", "检测过程提示信息："))

