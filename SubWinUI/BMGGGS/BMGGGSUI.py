# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMGGGSUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BMGGGSForm(object):
    def setupUi(self, BMGGGSForm):
        BMGGGSForm.setObjectName("BMGGGSForm")
        BMGGGSForm.resize(1006, 503)
        self.ProfileLineEdit = QtWidgets.QLineEdit(BMGGGSForm)
        self.ProfileLineEdit.setGeometry(QtCore.QRect(106, 58, 731, 31))
        self.ProfileLineEdit.setObjectName("ProfileLineEdit")
        self.JCBGLineEdit = QtWidgets.QLineEdit(BMGGGSForm)
        self.JCBGLineEdit.setGeometry(QtCore.QRect(96, 448, 751, 31))
        self.JCBGLineEdit.setObjectName("JCBGLineEdit")
        self.TipInfoLbl = QtWidgets.QLabel(BMGGGSForm)
        self.TipInfoLbl.setGeometry(QtCore.QRect(26, 98, 131, 16))
        self.TipInfoLbl.setObjectName("TipInfoLbl")
        self.ScanTextEdit = QtWidgets.QTextEdit(BMGGGSForm)
        self.ScanTextEdit.setGeometry(QtCore.QRect(26, 118, 961, 311))
        self.ScanTextEdit.setObjectName("ScanTextEdit")
        self.DoScanProfileBtn = QtWidgets.QPushButton(BMGGGSForm)
        self.DoScanProfileBtn.setGeometry(QtCore.QRect(856, 48, 131, 41))
        self.DoScanProfileBtn.setObjectName("DoScanProfileBtn")
        self.ProfileLbl = QtWidgets.QLabel(BMGGGSForm)
        self.ProfileLbl.setGeometry(QtCore.QRect(26, 58, 81, 31))
        self.ProfileLbl.setObjectName("ProfileLbl")
        self.ReportLbl = QtWidgets.QLabel(BMGGGSForm)
        self.ReportLbl.setGeometry(QtCore.QRect(26, 448, 71, 31))
        self.ReportLbl.setObjectName("ReportLbl")
        self.ViewReportBtn = QtWidgets.QPushButton(BMGGGSForm)
        self.ViewReportBtn.setGeometry(QtCore.QRect(860, 440, 131, 41))
        self.ViewReportBtn.setObjectName("ViewReportBtn")

        self.retranslateUi(BMGGGSForm)
        QtCore.QMetaObject.connectSlotsByName(BMGGGSForm)

    def retranslateUi(self, BMGGGSForm):
        _translate = QtCore.QCoreApplication.translate
        BMGGGSForm.setWindowTitle(_translate("BMGGGSForm", "部门公告公示"))
        self.TipInfoLbl.setText(_translate("BMGGGSForm", "检测过程提示信息："))
        self.DoScanProfileBtn.setText(_translate("BMGGGSForm", "执行配置文件检测"))
        self.ProfileLbl.setText(_translate("BMGGGSForm", "配置文件："))
        self.ReportLbl.setText(_translate("BMGGGSForm", "检测报告："))
        self.ViewReportBtn.setText(_translate("BMGGGSForm", "查看检测报告"))

