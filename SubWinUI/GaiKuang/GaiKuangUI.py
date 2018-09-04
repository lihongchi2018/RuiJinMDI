# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GaiKuangUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GaiKuangForm(object):
    def setupUi(self, GaiKuangForm):
        GaiKuangForm.setObjectName("GaiKuangForm")
        GaiKuangForm.resize(1006, 523)
        self.ProfileLineEdit = QtWidgets.QLineEdit(GaiKuangForm)
        self.ProfileLineEdit.setGeometry(QtCore.QRect(106, 58, 731, 31))
        self.ProfileLineEdit.setObjectName("ProfileLineEdit")
        self.JCBGLineEdit = QtWidgets.QLineEdit(GaiKuangForm)
        self.JCBGLineEdit.setGeometry(QtCore.QRect(96, 448, 751, 31))
        self.JCBGLineEdit.setObjectName("JCBGLineEdit")
        self.TipInfoLbl = QtWidgets.QLabel(GaiKuangForm)
        self.TipInfoLbl.setGeometry(QtCore.QRect(26, 98, 131, 16))
        self.TipInfoLbl.setObjectName("TipInfoLbl")
        self.ScanTextEdit = QtWidgets.QTextEdit(GaiKuangForm)
        self.ScanTextEdit.setGeometry(QtCore.QRect(26, 118, 961, 311))
        self.ScanTextEdit.setObjectName("ScanTextEdit")
        self.DoScanProfileBtn = QtWidgets.QPushButton(GaiKuangForm)
        self.DoScanProfileBtn.setGeometry(QtCore.QRect(856, 48, 131, 41))
        self.DoScanProfileBtn.setObjectName("DoScanProfileBtn")
        self.ProfileLbl = QtWidgets.QLabel(GaiKuangForm)
        self.ProfileLbl.setGeometry(QtCore.QRect(26, 58, 81, 31))
        self.ProfileLbl.setObjectName("ProfileLbl")
        self.ReportLbl = QtWidgets.QLabel(GaiKuangForm)
        self.ReportLbl.setGeometry(QtCore.QRect(26, 448, 71, 31))
        self.ReportLbl.setObjectName("ReportLbl")
        self.ViewReportBtn = QtWidgets.QPushButton(GaiKuangForm)
        self.ViewReportBtn.setGeometry(QtCore.QRect(860, 440, 131, 41))
        self.ViewReportBtn.setObjectName("ViewReportBtn")

        self.retranslateUi(GaiKuangForm)
        QtCore.QMetaObject.connectSlotsByName(GaiKuangForm)

    def retranslateUi(self, GaiKuangForm):
        _translate = QtCore.QCoreApplication.translate
        GaiKuangForm.setWindowTitle(_translate("GaiKuangForm", "部门概况"))
        self.TipInfoLbl.setText(_translate("GaiKuangForm", "检测过程提示信息："))
        self.DoScanProfileBtn.setText(_translate("GaiKuangForm", "执行配置文件检测"))
        self.ProfileLbl.setText(_translate("GaiKuangForm", "配置文件："))
        self.ReportLbl.setText(_translate("GaiKuangForm", "检测报告："))
        self.ViewReportBtn.setText(_translate("GaiKuangForm", "查看检测报告"))

