# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget,QMessageBox,QMainWindow
from PyQt5.QtGui import QStandardItemModel,QStandardItem
import os


class LoadTableData(QWidget):
    def __init__(self, UIBtn, UI, MainWindow):
        super(LoadTableData, self).__init__()
        self.initUi(UIBtn, UI, MainWindow)

    def initUi(self, UIBtn, UI, MainWindow):
        currPath = "./RuiJinModule/XXGKStaticInfo"
        # 1、判断是否有配置文件，以及是否生成默认配置文件
        ProfilePath = "/Profile/bmgkxx_XXGKStaticInfo.profile"
        if os.path.exists(currPath + ProfilePath):
            #定义检测需要的列表对象
            #bmlink_list为配置文件中的链接地址列表，bmlink_title为前列表的标题或说明列表，
            bmlink_list,bmlink_title_list = [],[]
            ColumnTimeLimit = { }

            # 2、扫描配置文件中的链接，并保存到bmlink_list,bmlink_title中,并将栏目更新天数保存到ColumnTimeLimit中
            with open(currPath + ProfilePath, 'r+') as fr:
                for line in fr.readlines():
                    linestr = line.strip()
                    if (linestr[0:1] == "#"):
                        if(linestr[0:2] == "##"):
                            #UI.ScanTextEdit.append("此行为栏目更新时限设置：" + linestr[2:linestr.index(":")] + " 更新时限为" + linestr[linestr.index(":")+1:] + "天")
                            ColumnTimeLimit[linestr[2:linestr.index(":")]] = linestr[linestr.index(":")+1:]
                        else:
                            #UI.ScanTextEdit.append("此行为注释：" + linestr)
                            pass
                    elif (linestr == ""):
                        #UI.ScanTextEdit.append("此行为空")
                        pass
                    else:
                        #UI.ScanTextEdit.append(linestr)
                        iLinkPosEnd = linestr.index(":", 5)
                        lLinkTxtPosEnd = len(linestr)
                        bmlink_list.append(linestr[0:iLinkPosEnd])
                        bmlink_title_list.append(linestr[iLinkPosEnd + 1:lLinkTxtPosEnd])
        else:
            QMessageBox.information(self, "提示标题", "无配置文件", QMessageBox.Yes | QMessageBox.No)

        # 准备数据模型
        profile_model = QStandardItemModel()

        profile_model.setHorizontalHeaderItem(0, QStandardItem("栏目名"))
        profile_model.setHorizontalHeaderItem(1, QStandardItem("栏目地址"))
        profile_model.setHorizontalHeaderItem(2, QStandardItem("更新天数要求"))
        profile_model.setHorizontalHeaderItem(3, QStandardItem("说明或操作"))

        index_tmp = 0
        for eachbmlink in bmlink_list:
            profile_model.setItem(index_tmp, 1, QStandardItem(eachbmlink))
            profile_model.setItem(index_tmp, 0, QStandardItem(bmlink_title_list[index_tmp]))
            if (bmlink_title_list[index_tmp] in ColumnTimeLimit):
                daystr = ColumnTimeLimit[bmlink_title_list[index_tmp]]
                profile_model.setItem(index_tmp, 2, QStandardItem(daystr))
            else:
                # 默认使用365天
                profile_model.setItem(index_tmp, 2, QStandardItem("365"))
            profile_model.setItem(index_tmp, 3,QStandardItem('请手动查阅并更新') )
            index_tmp = index_tmp + 1

        # 利用setModel()方法将数据模型与QTableView绑定
        UI.DataTableView.setModel(profile_model)
        # 设置表格的各列的宽度值
        UI.DataTableView.setColumnWidth(0, 200)
        UI.DataTableView.setColumnWidth(1, 350)
        UI.DataTableView.setColumnWidth(3, 200)
