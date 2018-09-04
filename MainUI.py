# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBMGKIndex = QtWidgets.QAction(MainWindow)
        self.actionBMGKIndex.setObjectName("actionBMGKIndex")
        self.actionBMGaiKuang = QtWidgets.QAction(MainWindow)
        self.actionBMGaiKuang.setObjectName("actionBMGaiKuang")
        self.actionXXGKIndexColumn = QtWidgets.QAction(MainWindow)
        self.actionXXGKIndexColumn.setObjectName("actionXXGKIndexColumn")
        self.actionXXGKStaticInfo = QtWidgets.QAction(MainWindow)
        self.actionXXGKStaticInfo.setObjectName("actionXXGKStaticInfo")
        self.actionBMGGGS = QtWidgets.QAction(MainWindow)
        self.actionBMGGGS.setObjectName("actionBMGGGS")
        self.menu.addAction(self.actionBMGKIndex)
        self.menu.addAction(self.actionBMGaiKuang)
        self.menu.addAction(self.actionBMGGGS)
        self.menu.addAction(self.actionXXGKIndexColumn)
        self.menu.addAction(self.actionXXGKStaticInfo)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "瑞金政府网检测"))
        self.menu.setTitle(_translate("MainWindow", "政府信息公开检测模块"))
        self.menu_2.setTitle(_translate("MainWindow", "政府网站检测模块"))
        self.actionBMGKIndex.setText(_translate("MainWindow", "部门首页"))
        self.actionBMGaiKuang.setText(_translate("MainWindow", "部门概况"))
        self.actionXXGKIndexColumn.setText(_translate("MainWindow", "信息公开首页栏目"))
        self.actionXXGKStaticInfo.setText(_translate("MainWindow", "静态信息检测表"))
        self.actionBMGGGS.setText(_translate("MainWindow", "部门公告公示"))

