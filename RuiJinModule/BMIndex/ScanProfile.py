# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget,QMessageBox,QMainWindow
import os,time
import urllib.request
import threading

#自定义函数
from RuiJinPublicClass.PublicClass import mkdir
from RuiJinModule.BMIndex.ScanBMIndexPage import getAllLinkHTML
import win32api


class ScanBMXXGK(QWidget):
    def __init__(self, UIBtn, UI, MainWindow):
        super(ScanBMXXGK, self).__init__()
        self.initUi(UIBtn, UI, MainWindow)

    def initUi(self, UIBtn, UI, MainWindow):
        UI.ScanTextEdit.append("Start BMIndex Module ... ...")
        currPath="./RuiJinModule/BMIndex"
        # 1、定义要创建的bmxxgkTest,bmxxgkLinkTest,bmxxgkLinkHttpTest,bmxxgkLinkHttpStatusTest,bmxxgkbg
        mkpath = ['bmxxgkTest', 'bmxxgkLinkTest', 'bmxxgkLinkHttpTest', 'bmxxgkLinkHttpStatusTest', 'bmxxgkbg']
        # 调用函数
        UI.ScanTextEdit.append("创建检测文件夹，文件夹放在" + currPath + "/jcbg/下   ...\n" + (" | ".join(mkpath)))
        for eachpath in mkpath:
            mkdir(currPath+ "/jcbg/" + eachpath.strip())

        # 2、判断是否有配置文件，以及是否生成默认配置文件
        if os.path.exists(currPath+"/Profile/bmgkxx_list.profile"):
            UI.ScanTextEdit.append("准备扫描配置文件中的链接... ...")
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
                with open(currPath + "/Profile/bmgkxx_list.profile", 'w+') as fw:
                    fw.write("\n".join(profile_list))
            else:
                UI.ScanTextEdit.append("取消生成配置文件。")

        # 如果有配置文件，则进行对配置文件中的链接进行扫描
        if os.path.exists(currPath + "/Profile/bmgkxx_list.profile"):
            #定义检测需要的列表对象
            #bmlink_list为配置文件中的链接地址列表，bmlink_title为前列表的标题或说明列表，
            #bm_httpstatus_file为链接是否能访问状态列表，link_list_file为配置文件中链接的页面文件列表
            bmlink_list,bmlink_title_list,bm_httpstatus_file,link_list_file = [],[],[],[]

            # 3、扫描配置文件中的链接，并保存到bmlink_list,bmlink_title中
            with open(currPath + '/Profile/bmgkxx_list.profile', 'r+') as fr:
                for line in fr.readlines():
                    linestr = line.strip()
                    if (linestr[0:1] == "#"):
                        UI.ScanTextEdit.append("此行为注释：" + linestr)
                    elif (linestr == ""):
                        UI.ScanTextEdit.append("此行为空")
                    else:
                        UI.ScanTextEdit.append(linestr)
                        iLinkPosEnd = linestr.index(":", 5)
                        lLinkTxtPosEnd = len(linestr)
                        bmlink_list.append(linestr[0:iLinkPosEnd])
                        bmlink_title_list.append(linestr[iLinkPosEnd + 1:lLinkTxtPosEnd])

            # 4、遍历信息公开首页，判断链接是否可用
            UI.ScanTextEdit.append("开始检测配置文件第一个链接，一般为网站根域名。")
            url = ""
            try:
                url = bmlink_list[0].strip()
                req = urllib.request.Request(url)
                response = urllib.request.urlopen(req)
                # 这就是获取返回的状态码 404 200等
                UI.ScanTextEdit.append(url + " status code:" + str(response.getcode()))
            except:
                UI.ScanTextEdit.append(url + ",urllib Except。\n首页检测异常，直接返回，不执行后续相关链接。")
                reply = QMessageBox.information(self, "提示标题", "首页检测异常，是否要继续检测其他链接？", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    UI.ScanTextEdit.append("继续检测其他链接。")
                else:
                    UI.ScanTextEdit.append("结束链接检测，返回。")
                    return

            # 写入原HTML文件，文件名格式为当前日期，FileName_time_list为存储链接文件列表
            FileName_time = time.strftime("%Y_%m_%d", time.localtime())
            FileName_time_int = int(time.strftime("%Y%m%d", time.localtime()))
            FileName_time_list = []
            link_list_http_file = []
            # 遍历各部门首页，并抓取各部门的网页保存。创建新线程来处理，避免界面出现等待情况
            ScanThread = threading.Thread(target=getAllLinkHTML, args=(currPath,
                UI,link_list_http_file, bmlink_list, bmlink_title_list, bm_httpstatus_file, link_list_file, FileName_time,
                FileName_time_int, FileName_time_list))
            ScanThread.start()
        else:
            UI.ScanTextEdit.append("未找到配置文件，扫描取消。")

#查看扫描检测报告
def ViewReport(UIBtn, UI, MainWindow):
    UI.ScanTextEdit.append(UI.JCBGLineEdit.text())
    returnvalue = win32api.ShellExecute(0, "open", UI.JCBGLineEdit.text(), None, "", 0)
    UI.ScanTextEdit.append("打开文件返回值："+ str(returnvalue))