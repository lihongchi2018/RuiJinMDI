# -*- coding: utf-8 -*-
'''
遍历各部门首页链接，并抓取页面html文档保存
'''

from RuiJinModule.GaiKuang.ScanPageHtml import getLinkHTML,getIndexHtmlLink,FormatLink
from RuiJinModule.GaiKuang.ScanHttpLink import ScanPageLink
from RuiJinModule.GaiKuang.MakeReport import ScanReport

#检测配置文件中的链接，并生成检测报告
# mkpath = ['bmxxgkTest', 'bmxxgkLinkTest', 'bmxxgkLinkHttpTest', 'bmxxgkLinkHttpStatusTest', 'bmxxgkbg']
def getAllLinkHTML(currPath,UI,link_list_http_file,bmlink_list,bmlink_title_list,bm_httpstatus_file,link_list_file,
                  FileName_time,FileName_time_int, FileName_time_list):
    iTmp = 0
    #1、获取指定链接的HTML内容，并保存至文件中bmxxgkTest
    for eachlink in bmlink_list:
        strTmp = eachlink
        try:
            strTmp = getLinkHTML(currPath,iTmp, bmlink_list, bmlink_title_list, FileName_time, FileName_time_list)
        except:
            strTmp = strTmp + ":检测此链接出现异常。"
        UI.ScanTextEdit.append(strTmp)
        iTmp = iTmp + 1
    UI.ScanTextEdit.append("扫描配置文件中的链接总数为: " + str(iTmp) + " 个")

    # 2、将页面链接提取到文件中bmxxgkLinkTest
    UI.ScanTextEdit.append("准备将页面链接提取到文件中......")
    strTmp = getIndexHtmlLink(currPath,bmlink_title_list, FileName_time, FileName_time_list, link_list_file)
    UI.ScanTextEdit.append(strTmp)

    # 3、将页面链接格式化链接为http://格式到文件中bmxxgkLinkHttpTest
    UI.ScanTextEdit.append("准备将页面链接格式化链接为http://格式到文件中......")
    strTmp = FormatLink(currPath,link_list_file, bmlink_list, bmlink_title_list, FileName_time,link_list_http_file)
    UI.ScanTextEdit.append(strTmp)

    #4、开始检查网站链接是否能访问bmxxgkLinkHttpStatusTest
    UI.ScanTextEdit.append("准备开始检查网站链接是否能访问......")
    strTmp = ScanPageLink(currPath,UI,link_list_http_file,bmlink_title_list,bmlink_list,bm_httpstatus_file,FileName_time)
    UI.ScanTextEdit.append(strTmp)

    #5、写入检测报告到文件中bmxxgkbg
    UI.ScanTextEdit.append("准备写入检测报告到文件中......")
    strTmp = ScanReport(currPath,UI,bm_httpstatus_file,FileName_time_int,bmlink_title_list,FileName_time,bmlink_list)
    UI.ScanTextEdit.append(strTmp)
    UI.ScanTextEdit.append("所有检测完毕，请查看下面检测报告。")


