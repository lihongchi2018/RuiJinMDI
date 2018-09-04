# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget,QMessageBox,QMainWindow
import os,time
import urllib.request

#自定义函数
from RuiJinPublicClass.PublicClass import mkdir

'''
加载配置文件
'''

class ScanXXGKStaticInfo(QWidget):
    def __init__(self, UIBtn, UI, MainWindow):
        super(ScanXXGKStaticInfo, self).__init__()
        self.initUi(UIBtn, UI, MainWindow)

    def initUi(self, UIBtn, UI, MainWindow):
        #UI.ScanTextEdit.append("Start XXGKStaticInfo Module ... ...")
        currPath="./RuiJinModule/XXGKStaticInfo"
        # 1、判断是否有配置文件，以及是否生成默认配置文件
        ProfilePath = "/Profile/bmgkxx_XXGKStaticInfo.profile"
        if os.path.exists(currPath + ProfilePath ):
            #UI.ScanTextEdit.append("准备扫描配置文件中的链接... ...")
            pass
        else:
            UI.ScanTextEdit.append("找不到配置文件bmgkxx_list.profile，配置文件样式如下：")
            UI.ScanTextEdit.append("#链接地址:单位名称")
            UI.ScanTextEdit.append("http://xxgk.ruijin.gov.cn/:市人民政府信息公开")
            UI.ScanTextEdit.append("http://xxgk.ruijin.gov.cn/bmgkxx/szfbgs/:市人民政府办公室")
            UI.ScanTextEdit.append("http://xxgk.ruijin.gov.cn/bmgkxx/jmw/:市工业和信息化局")
            profile_list = []
            profile_list.append("http://xxgk.ruijin.gov.cn/:市人民政府信息公开")
            profile_list.append("http://xxgk.ruijin.gov.cn/bmgkxx/szfbgs/:市人民政府办公室")
            profile_list.append("http://xxgk.ruijin.gov.cn/bmgkxx/jmw/:市工业和信息化局")

            reply = QMessageBox.information(self, "提示标题", "是否生成默认配置文件？", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                mkdir(currPath + "/Profile")
                with open(currPath + ProfilePath, 'w+') as fw:
                    fw.write("\n".join(profile_list))
            else:
                UI.ScanTextEdit.append("取消生成配置文件。")

        # 如果有配置文件，则进行对配置文件中的链接进行扫描
        if os.path.exists(currPath + ProfilePath):
            #定义检测需要的列表对象
            #bmlink_list为配置文件中的链接地址列表，bmlink_title为前列表的标题或说明列表，
            #bm_httpstatus_file为链接是否能访问状态列表，link_list_file为配置文件中链接的页面文件列表
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
                        UI.ScanTextEdit.append(linestr)
                        iLinkPosEnd = linestr.index(":", 5)
                        lLinkTxtPosEnd = len(linestr)
                        bmlink_list.append(linestr[0:iLinkPosEnd])
                        bmlink_title_list.append(linestr[iLinkPosEnd + 1:lLinkTxtPosEnd])
        else:
            UI.ScanTextEdit.append("未找到配置文件")
