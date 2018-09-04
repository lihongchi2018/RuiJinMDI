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