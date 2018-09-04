# -*- coding: utf-8 -*-
'''
检查网站链接是否能访问，并将检测结果写入文件
'''
import urllib.request,urllib.error,time,re,datetime,os

#该函数功能为检查页面中提取的格式化的链接是否能访问，并写入到文件中
def ScanPageLink(currPath,UI,link_list_http_file,bmlink_title_list,bmlink_list,bm_httpstatus_file,FileName_time):
    iTmp = 0
    print('开始检查网站链接是否能访问')
    print("检测文件数:" + str(len(link_list_http_file)))
    UI.ScanTextEdit.append("检测已格式化链接为http://的链接文件数:" + str(len(link_list_http_file)))
    #ilen = len(link_list_http_file)
    for eachstr in link_list_http_file:
        link_list = []
        link_list_status = []
        with open(link_list_http_file[iTmp],'rb') as fr:
            for line in fr.readlines():
                link_list.append(line.decode('utf-8').strip())
                link_list_status.append("000")#未检测标记
        print( "读取文件" + link_list_http_file[iTmp] + ",准备测试" + bmlink_title_list[iTmp] + ":")
        print('开始检查内部网站链接：')
        jTmp = 0
        for eachlink in link_list:
            print(eachlink)
            if ("?lhc_titleName=" in eachlink):
                eachlink = eachlink[0:eachlink.find("?lhc_titleName=")+1]
                print(eachlink)
                #raw_input("press key any to continue ...")
            if("#" in eachlink):
                eachlink = eachlink[0:eachlink.find("#")]
                print(eachlink)
                #raw_input("press key any to continue ...")
            jTmp = jTmp + 1
            #判断是否为内部链接
            print("#判断是否为内部链接" + bmlink_list[0].strip())
            #raw_input("press key any to continue ...")
            if(bmlink_list[0].strip() in eachlink):
                try:
                    req = urllib.request.Request(eachlink)
                    response = urllib.request.urlopen(req, timeout=1)
                    link_list_status[jTmp-1] = str(response.getcode())
                    print(str(jTmp) + ". " + eachlink + ": return_code = " + str(response.getcode())) #这就是获取返回的状态码 404 200等
                except IOError:
                    link_list_status[jTmp-1] = "000"
                    print(str(jTmp) + ". " + eachlink + " : urllib IOError")
                finally:
                    #time.sleep(0.01)
                    pass
        print('开始检查外部网站链接：')
        #跳过检测外部网站
        out_link_flag = "y"
        #out_link_flag = raw_input("是否要测试外部链接，输入y，继续测试，否则直接通过:")
        jTmp = 0
        if (out_link_flag == "y"):
            for eachlink in link_list:
                print(eachlink)
                #raw_input("press key any to continue ...")
                if ("?lhc_titleName=" in eachlink):
                    eachlink = eachlink[0:eachlink.find("?lhc_titleName=")+1]
                    print(eachlink)
                    #raw_input("press key any to continue ...")
                if("#" in eachlink):
                    eachlink = eachlink[0:eachlink.find("#")]
                    print(eachlink)
                    #raw_input("press key any to continue ...")
                jTmp = jTmp + 1
                if( eachlink[0:7] == "http://" ):
                    if(bmlink_list[0].strip() not in eachlink):
                        try:
                            #print "\n外链测试：" + eachlink
                            req = urllib.request.Request(eachlink)
                            response = urllib.request.urlopen(req, timeout=1)
                            link_list_status[jTmp-1] = str(response.getcode())
                            print(str(jTmp) + ". " + eachlink + ": return_code = " + str(response.getcode())) #这就是获取返回的状态码 404 200等
                        except IOError:
                            link_list_status[jTmp-1] = "000"
                            print(str(jTmp) + ". " + eachlink + " : urllib IOError")
                        finally:
                            #time.sleep(0.1)
                            pass
                else:
                    #将非http类型的链接放弃测试，直接通过
                    #raw_input("检测到非http协议，直接通过")
                    link_list_status[jTmp-1] = "200"
                    print(str(jTmp) + ". " + eachlink + ": return_code = 200")  #不检测javascript类型的链接
        else:
            if(bmlink_list[0].strip() not in eachlink):
                for eachlink in link_list:
                    jTmp = jTmp + 1
                    link_list_status[jTmp-1] = "200"
                    print(str(jTmp) + ". " + eachlink + ": return_code = 200") #这就是获取返回的状态码 404 200等
        print("测试" + bmlink_title_list[iTmp] + "完成！")
        #将检测结果写入文件中
        list_status_toFile = []
        jTmp = 0
        for eachListList in link_list:
            list_status_toFile.append(link_list_status[jTmp] + ":" + eachListList)
            jTmp = jTmp + 1
        strLinkListFile_http_status = currPath + '/jcbg/bmxxgkLinkHttpStatusTest/' + bmlink_title_list[iTmp] + FileName_time + ".html"
        bm_httpstatus_file.append(strLinkListFile_http_status)
        with open(strLinkListFile_http_status,'wb') as fw:
            fw.write(("\n".join(list_status_toFile)).encode('utf-8'))
            print("检测结果写入文件中完成！" + bmlink_title_list[iTmp])
        iTmp = iTmp +1
        #raw_input("press key any to continue ...")
        UI.ScanTextEdit.append(eachstr+"文件检测完毕！")
    print("All test ok!")
    return "所有格式化后的链接文件测试结束。"

#该函数功能分析各单位检测状态文件，生成检测报告，并写入到文件中
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
    							<div style='text-align:center;font-size:22px;'>网站首页检测报告</div>
    							<div style ="text-align:center;font-size:16px;">报表生成日期：							
    					"""
    bm_bg_str_head = bm_bg_str_head + str(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime()))
    bm_bg_str_head = bm_bg_str_head + """（首页更新日期以文件创建时间计算）		
    							</div>
    							<div style='text-align:center;'><table style='margin-top:10px;width:1000px;'>
    								<tr><th>序号</th><th>单位名称</th><th>首页动态更新日期</th><th>是否两周内更新</th><th>首页不能访问链接数</th><th>详细报告</th></tr>
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
                if ("/gzdt/" in statuslinktmp):
                    # raw_input("Test gzdt/zwdt")
                    res = r'/t2.*_.*?.htm'
                    getLinkDate = re.findall(res, statuslinktmp, re.I | re.S | re.M)
                    if len(getLinkDate):
                        for var in getLinkDate:
                            # print var
                            if len(var) > 10:
                                if int(var[2:10]) > date_str_int:
                                    date_str_int = int(var[2:10])
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
                if delta.days < 14:
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
    #current_path = os.path.abspath(__file__)
    current_path = os.getcwd() + "\\RuiJinModule\\BMIndex"
    #UI.ScanTextEdit.append(current_path + " == current_path")
    #UI.ScanTextEdit.append(os.getcwd() + " == current_path")
    # 获取当前文件的父目录
    UI.JCBGLineEdit.setText(current_path + '\\jcbg\\部门信息公开检测报告' + FileName_time + ".html.xls" )
    return "配置文件检测报告生成完毕！"