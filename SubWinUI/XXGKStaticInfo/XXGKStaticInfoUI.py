# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XXGKStaticInfoUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XXGKStaticInfoForm(object):
    def setupUi(self, XXGKStaticInfoForm):
        XXGKStaticInfoForm.setObjectName("XXGKStaticInfoForm")
        XXGKStaticInfoForm.resize(1012, 551)
        self.ProfileLineEdit = QtWidgets.QLineEdit(XXGKStaticInfoForm)
        self.ProfileLineEdit.setGeometry(QtCore.QRect(106, 58, 731, 31))
        self.ProfileLineEdit.setObjectName("ProfileLineEdit")
        self.TipInfoLbl = QtWidgets.QLabel(XXGKStaticInfoForm)
        self.TipInfoLbl.setGeometry(QtCore.QRect(26, 98, 131, 16))
        self.TipInfoLbl.setObjectName("TipInfoLbl")
        self.ScanTextEdit = QtWidgets.QTextEdit(XXGKStaticInfoForm)
        self.ScanTextEdit.setGeometry(QtCore.QRect(26, 118, 961, 131))
        self.ScanTextEdit.setObjectName("ScanTextEdit")
        self.DoScanProfileBtn = QtWidgets.QPushButton(XXGKStaticInfoForm)
        self.DoScanProfileBtn.setGeometry(QtCore.QRect(856, 48, 131, 41))
        self.DoScanProfileBtn.setObjectName("DoScanProfileBtn")
        self.ProfileLbl = QtWidgets.QLabel(XXGKStaticInfoForm)
        self.ProfileLbl.setGeometry(QtCore.QRect(26, 58, 81, 31))
        self.ProfileLbl.setObjectName("ProfileLbl")
        self.DataTableView = QtWidgets.QTableView(XXGKStaticInfoForm)
        self.DataTableView.setGeometry(QtCore.QRect(26, 260, 961, 201))
        self.DataTableView.setObjectName("DataTableView")
        self.LoadDataTableBtn = QtWidgets.QPushButton(XXGKStaticInfoForm)
        self.LoadDataTableBtn.setGeometry(QtCore.QRect(834, 472, 141, 41))
        self.LoadDataTableBtn.setObjectName("LoadDataTableBtn")

        self.retranslateUi(XXGKStaticInfoForm)
        QtCore.QMetaObject.connectSlotsByName(XXGKStaticInfoForm)

    def retranslateUi(self, XXGKStaticInfoForm):
        _translate = QtCore.QCoreApplication.translate
        XXGKStaticInfoForm.setWindowTitle(_translate("XXGKStaticInfoForm", "信息公开静态信息检测"))
        self.TipInfoLbl.setText(_translate("XXGKStaticInfoForm", "静态页面配置信息："))
        self.DoScanProfileBtn.setText(_translate("XXGKStaticInfoForm", "加载配置文件"))
        self.ProfileLbl.setText(_translate("XXGKStaticInfoForm", "配置文件："))
        self.LoadDataTableBtn.setText(_translate("XXGKStaticInfoForm", "导入配置文件到表格中"))

