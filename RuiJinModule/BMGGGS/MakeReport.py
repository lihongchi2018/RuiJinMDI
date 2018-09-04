# -*- coding: utf-8 -*-

import time,re,datetime,os


'''
#分析各单位检测状态文件，生成检测报告，并写入到文件中
'''
def ScanReport(currPath,UI,bm_httpstatus_file,FileName_time_int,bmlink_title_list,FileName_time,bmlink_list):
    print("开始分析各单位检测状态文件")
    #bm_bg_list为所有部门汇总检测报告html列表对象
    bm_bg_list = []
    #所有部门汇总检测报告头部html模板
    bm_bg_str_head = """
    				<!DOCTYPE html>
    					<html>
    					<head>
    					<meta charset="utf-8"> 
    					<title>数据汇总报告</title>
    					<style>
    					table, td, th{border:1px solid green;text-align:left;}
    					th{background-color:gray;color:white;}
    					body{margin:0 auto;text-align:center;width:1024px;}
    					</style>
    					</head>
    					<body>
    						<div style='margin:0 auto;text-align:center;margin-top:20px;'>
    							<div style='text-align:center;font-size:22px;'>部门公告公示栏目检测报告</div>
    							<div style ="text-align:center;font-size:16px;">报表生成日期：							
    					"""
    bm_bg_str_head = bm_bg_str_head + str(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime()))
    bm_bg_str_head = bm_bg_str_head + """（首页更新日期以文件创建时间计算）		
    							</div>
    							<div style='text-align:center;'><table style='margin-top:10px;width:1000px;'>
    								<tr><th>序号</th><th>单位名称</th><th>首页动态更新日期</th><th>是否及时更新</th><th>首页不能访问链接数</th><th>详细报告</th></tr>
    					 """
    bm_bg_list.append(bm_bg_str_head)

    #各部门栏目检测html模板bm_bg_html_header，bm_bg_html_tailer
    bm_bg_html_header = """
    				<!DOCTYPE html>
    					<html>
    					<head>
    					<meta charset="utf-8"> 
    					<title>网站栏目检测报告</title>
    					<style>
    					table, td, th{border:1px solid green;text-align:left;}
    					th{background-color:gray;color:white;}
    					body{margin:0 auto;text-align:center;width:1024px;}
    					</style>
    					</head>
    					<body>
    						<div style='margin:0 auto;text-align:center;margin-top:20px;'>
    					"""
    bm_bg_html_tailer = """
    						</div>
    					</body>
    					</html>
    						"""
    iTmp = 0
    # print str(len(bm_httpstatus_file))
    for status_file in bm_httpstatus_file:
        print(status_file.strip())
        status_link_list = []
        bmxxgkbg_list = []
        with open(status_file, 'rb') as fr:
            bm_bg_html_content = ""
            lhc_xuhao = 1
            #分析链接类型
            for line in fr.readlines():
                # print line.strip()
                strhtmlcontent = line.decode('utf-8').strip()
                status_link_list.append(strhtmlcontent)
                bm_bg_html_content = bm_bg_html_content + "<tr><td>" + str(lhc_xuhao) + "</td><td>" + strhtmlcontent[
                                                                                                      0:3] + "</td>"
                lhc_linkhref = strhtmlcontent[4:len(strhtmlcontent)]
                lhc_linktxt = strhtmlcontent[4:len(strhtmlcontent)]
                if ("?lhc_titleName=" in strhtmlcontent):
                    lhc_linkhref = strhtmlcontent[4:strhtmlcontent.find("?lhc_titleName=") + 1]
                    lhc_linktxt = strhtmlcontent[strhtmlcontent.find("?lhc_titleName=") + 15:len(strhtmlcontent)]
                # raw_input("press any key ... ")
                bm_bg_html_content = bm_bg_html_content + "<td><a href='" + lhc_linkhref + "'>" + lhc_linktxt + "</a></td>"
                res = r'/t2.*_.*?.htm'
                getLinkDate = re.findall(res, strhtmlcontent, re.I | re.S | re.M)
                lhc_date_str = "目录或其它"
                if len(getLinkDate):
                    for var in getLinkDate:
                        # print var
                        if len(var) > 10:
                            lhc_date_str = var[2:10]
                        if ("DocDate" in strhtmlcontent):
                            linkLen = len(strhtmlcontent)
                            lhc_date_str = strhtmlcontent[linkLen - 10:linkLen - 6] + strhtmlcontent[linkLen - 5:linkLen - 3] + strhtmlcontent[linkLen - 2:linkLen]
                bm_bg_html_content = bm_bg_html_content + "<td>" + lhc_date_str + "</td><td>"
                if strhtmlcontent[0:3] == "200":
                    bm_bg_html_content = bm_bg_html_content + "是</td></tr>"
                else:
                    bm_bg_html_content = bm_bg_html_content + "<span style='color:red;'>否</span></td></tr>"
                lhc_xuhao = lhc_xuhao + 1
            # 分析更新日期和错误链接
            ilink_error_num = 0
            date_str_int = 0
            for statuslinktmp in status_link_list:
                print(statuslinktmp)
                res = r'/t2.*_.*?.htm'
                getLinkDate = re.findall(res, statuslinktmp, re.I | re.S | re.M)
                DocDate = 0
                if("DocDate" in statuslinktmp):
                    linkLen = len(statuslinktmp)
                    DocDate = int(statuslinktmp[linkLen-10:linkLen-6] + statuslinktmp[linkLen-5:linkLen-3] + statuslinktmp[linkLen-2:linkLen])
                if len(getLinkDate):
                    for var in getLinkDate:
                        # print var
                        if len(var) > 10:
                            if int(var[2:10]) > date_str_int:
                                date_str_int = int(var[2:10])
                            if DocDate > date_str_int :
                                date_str_int = DocDate
                # print statuslinktmp[0:len(statuslinktmp)]
                if statuslinktmp[0:3] != "200":
                    ilink_error_num = ilink_error_num + 1
            strUpdateStatus = "<span style='color:red;'>否</span>"
            # 计算日期差
            if date_str_int == 0:
                pass
            else:
                d1 = datetime.datetime.strptime(str(date_str_int), '%Y%m%d')
                d2 = datetime.datetime.strptime(str(FileName_time_int), '%Y%m%d')
                delta = d2 - d1
                # print d1
                # print d2
                # print delta.days
                # raw_input("t")
                '''
                if delta.days < 14:
                    strUpdateStatus = "两周内"
                elif delta.days > 14 and delta.days < 90:
                    strUpdateStatus = "三个月内"
                elif delta.days > 90 and delta.days < 120:
                    strUpdateStatus = "三个月未更新<span style='color:red;'><br>离六个月时间还差" + str(120 - delta.days) + "天</span>"
                elif delta.days > 120 and delta.days < 365:
                    strUpdateStatus = "半年未更新<span style='color:red;'><br>离一年时间还差" + str(365 - delta.days) + "天</span>"
                elif delta.days > 365:
                    strUpdateStatus = "<span style='color:red;'>一年未更新</span>"
              '''
                if delta.days < 180:
                    strUpdateStatus = "是"
            bm_bg_html = "<div style='text-align:center;font-size:22px;'>" + bmlink_title_list[iTmp] + " 页面检测报告</div>"
            bm_bg_html = bm_bg_html + "<div style ='text-align:center;font-size:16px;'>报表生成日期：" + str(
                time.strftime("%Y_%m_%d %H:%M:%S", time.localtime()))
            bm_bg_html = bm_bg_html + " （链接状态200为正常，其它为异常）</div>"
            bm_bg_html = bm_bg_html + "<div style='text-align:center;'><table style='margin-top:10px;width:1000px;'>"
            bm_bg_html = bm_bg_html + "<tr><th>序号</th><th>链接状态</th><th>链接标题</th><th>文档创建日期</th><th>是否能访问</th></tr>"
            bm_bg_html = bm_bg_html_header + bm_bg_html + bm_bg_html_content + "</table></div>" + bm_bg_html_tailer
            # 写入各部门检测报告
            bmxxgkbg = currPath + '/jcbg/bmxxgkbg/' + str(iTmp) + "." + bmlink_title_list[iTmp] + FileName_time + ".html"
            bmxxgkbg_alink = './bmxxgkbg/' + str(iTmp) + "." + bmlink_title_list[iTmp] + FileName_time + ".html"
            bmxxgkbg_list.append(bmxxgkbg)
            with open(bmxxgkbg, 'wb') as fw:
                fw.write(bm_bg_html.encode('utf-8'))
                print("检测报告写入文件中完成！" + bmlink_title_list[iTmp])
            bm_bg_list.append(
                "<tr><td>" + str(iTmp + 1) + "</td><td><a href='" + bmlink_list[iTmp] + "'>" + bmlink_title_list[
                    iTmp] + "</a></td><td>" + str(date_str_int) + "</td><td>" + strUpdateStatus + "</td><td>" + str(
                    ilink_error_num) + "</td><td><a href='" + bmxxgkbg_alink + "'>" + bmxxgkbg_alink + "</a></td></tr>")
        iTmp = iTmp + 1
    bm_bg_list.append("</table></div></div></body></html>")
    bm_http_status_bg = currPath + '/jcbg/部门信息公开检测报告' + FileName_time + ".html"
    with open(bm_http_status_bg, 'wb') as fw:
        fw.write(("\n".join(bm_bg_list)).encode('utf-8'))
        print("检测报告写入文件中完成！" + bm_http_status_bg)
    with open(bm_http_status_bg + ".xls", 'wb') as fw:
        fw.write(("\n".join(bm_bg_list)).encode('utf-8'))
        print("检测报告写入文件中完成！" + bm_http_status_bg + ".xls")
    '''
   # 当前文件的路径
   pwd = os.getcwd()
   # 当前文件的父路径
   father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
   # 当前文件的前两级目录
   grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
    '''
    # 获取当前文件路径
    # current_path = os.path.abspath(__file__)
    current_path = os.getcwd() + "\\RuiJinModule\\BMGGGS"
    # UI.ScanTextEdit.append(current_path + " == current_path")
    # UI.ScanTextEdit.append(os.getcwd() + " == current_path")
    # 获取当前文件的父目录
    UI.JCBGLineEdit.setText(current_path + '\\jcbg\\部门信息公开检测报告' + FileName_time + ".html.xls")
    return "配置文件检测报告生成完毕！"