# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XXGKIndexColumnUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XXGKIndexColumnForm(object):
    def setupUi(self, XXGKIndexColumnForm):
        XXGKIndexColumnForm.setObjectName("XXGKIndexColumnForm")
        XXGKIndexColumnForm.resize(1006, 523)
        self.ProfileLineEdit = QtWidgets.QLineEdit(XXGKIndexColumnForm)
        self.ProfileLineEdit.setGeometry(QtCore.QRect(106, 58, 731, 31))
        self.ProfileLineEdit.setObjectName("ProfileLineEdit")
        self.JCBGLineEdit = QtWidgets.QLineEdit(XXGKIndexColumnForm)
        self.JCBGLineEdit.setGeometry(QtCore.QRect(96, 448, 751, 31))
        self.JCBGLineEdit.setObjectName("JCBGLineEdit")
        self.TipInfoLbl = QtWidgets.QLabel(XXGKIndexColumnForm)
        self.TipInfoLbl.setGeometry(QtCore.QRect(26, 98, 131, 16))
        self.TipInfoLbl.setObjectName("TipInfoLbl")
        self.ScanTextEdit = QtWidgets.QTextEdit(XXGKIndexColumnForm)
        self.ScanTextEdit.setGeometry(QtCore.QRect(26, 118, 961, 311))
        self.ScanTextEdit.setObjectName("ScanTextEdit")
        self.DoScanProfileBtn = QtWidgets.QPushButton(XXGKIndexColumnForm)
        self.DoScanProfileBtn.setGeometry(QtCore.QRect(856, 48, 131, 41))
        self.DoScanProfileBtn.setObjectName("DoScanProfileBtn")
        self.ProfileLbl = QtWidgets.QLabel(XXGKIndexColumnForm)
        self.ProfileLbl.setGeometry(QtCore.QRect(26, 58, 81, 31))
        self.ProfileLbl.setObjectName("ProfileLbl")
        self.ReportLbl = QtWidgets.QLabel(XXGKIndexColumnForm)
        self.ReportLbl.setGeometry(QtCore.QRect(26, 448, 71, 31))
        self.ReportLbl.setObjectName("ReportLbl")
        self.ViewReportBtn = QtWidgets.QPushButton(XXGKIndexColumnForm)
        self.ViewReportBtn.setGeometry(QtCore.QRect(860, 440, 131, 41))
        self.ViewReportBtn.setObjectName("ViewReportBtn")

        self.retranslateUi(XXGKIndexColumnForm)
        QtCore.QMetaObject.connectSlotsByName(XXGKIndexColumnForm)

    def retranslateUi(self, XXGKIndexColumnForm):
        _translate = QtCore.QCoreApplication.translate
        XXGKIndexColumnForm.setWindowTitle(_translate("XXGKIndexColumnForm", "信息公开首页栏目"))
        self.TipInfoLbl.setText(_translate("XXGKIndexColumnForm", "检测过程提示信息："))
        self.DoScanProfileBtn.setText(_translate("XXGKIndexColumnForm", "执行配置文件检测"))
        self.ProfileLbl.setText(_translate("XXGKIndexColumnForm", "配置文件："))
        self.ReportLbl.setText(_translate("XXGKIndexColumnForm", "检测报告："))
        self.ViewReportBtn.setText(_translate("XXGKIndexColumnForm", "查看检测报告"))

