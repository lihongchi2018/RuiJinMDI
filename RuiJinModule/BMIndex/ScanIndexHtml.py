# -*- coding: utf-8 -*-
'''
遍历各部门首页链接，并抓取页面html文档保存
'''
import sys,re
import urllib.request,urllib.error
import chardet

from urllib.parse import urljoin
from urllib.error import URLError, HTTPError

#该函数功能为获取指定链接的HTML内容，并保存至文件中
def getLinkHTML(currPath,ListNumber,bmlink_list,bmlink_title_list,FileName_time,FileName_time_list):
    returnStr = "start getLinkHTML ... "
    try:
        url = bmlink_list[ListNumber].strip()
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req,timeout=1)
        index_code = response.getcode()
        # 这就是获取返回的状态码 404 200等
        returnStr = url + " request status code:" + str(index_code)
        strTmp = currPath + '/jcbg/bmxxgkTest/' + bmlink_title_list[ListNumber] + FileName_time + ".html"
        FileName_time_list.append(strTmp)
        content = response.read()
        typeEncode = sys.getfilesystemencoding()  ##系统默认编码
        infoencode = chardet.detect(content).get('encoding', 'utf-8')  ##通过第3方模块来自动提取网页的编码
        #htmldata = content.decode(infoencode, 'ignore').encode(typeEncode)  ##先转换成unicode编码，然后转换系
        htmldata = content.decode(infoencode, 'ignore').encode(typeEncode)
        with open(strTmp, 'wb') as fw:
            try:
                fw.write(htmldata)
                returnStr = returnStr + " ,文件写入成功。"
            except:
                returnStr = bmlink_list[ListNumber].strip() + " : 写入文件异常"
    except HTTPError as e:
        print(e.code)
        returnStr = bmlink_list[ListNumber].strip() + e.code
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            returnStr = bmlink_list[ListNumber].strip() + e.reason
        elif hasattr(e, 'code'):
            print('The server could not fulfill the request.')
            print('Error code: ', e.code)
            returnStr = bmlink_list[ListNumber].strip() + e.reason
        else:
            print("good!")
            returnStr = bmlink_list[ListNumber].strip() + ":ok"
    except:
        returnStr = bmlink_list[ListNumber].strip() + " : urllib Except"
    print(returnStr)
    return returnStr

#该函数功能为将页面链接提取到文件中
def getIndexHtmlLink(currPath,bmlink_title_list,FileName_time,FileName_time_list,link_list_file):
    # 将页面链接提取到文件中
    iTmp = 0
    for link_file in FileName_time_list:
        with open(link_file, 'rb') as fr:
            htmldata = fr.read().decode('utf-8')
            res = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
            htmllinklist = re.findall(res,htmldata)
            print("页面a链接数："+ str(len(htmllinklist)))
            htmllinkdata = ""
            for eachlink in htmllinklist:
                linkurl,linktitle = eachlink
                htmllinkdata =htmllinkdata +"\n"+ linkurl + "?lhc_titleName=" + linktitle
                print(linkurl + ":"+ linktitle )
            strLinkListFile = currPath + '/jcbg/bmxxgkLinkTest/' + bmlink_title_list[iTmp] + FileName_time + ".html"
            link_list_file.append(strLinkListFile)
            # 将信息公开页面中类似
            # gkfs("主动公开","./gzdt/zwdt/201804/t20180424_408655.htm","我市今年安排24件民生实事")
            # 提取链接
            res = r'gkfs\(\".*?\"\)'
            script_link = re.findall(res, htmldata, re.I | re.S | re.M)
            script_link_list = []
            print("页面gkfs链接数：" + str(len(script_link)))
            if len(script_link):
                for eachlink in script_link:
                    # print eachlink
                    str_eachlink_arr = eachlink.strip().split(",")
                    linkTmp = str_eachlink_arr[1].strip()
                    linkTmp = linkTmp[1:len(linkTmp) - 1]
                    # print linkTmp
                    linkTitleTmp = str_eachlink_arr[2].strip()
                    linkTitleTmp = linkTitleTmp[1:len(linkTitleTmp) - 2]
                    # print linkTitleTmp
                    script_link_list.append(linkTmp + "?lhc_titleName=" + linkTitleTmp)
                    print(linkTmp + "?lhc_titleName=" + linkTitleTmp)
                # print linkTmp + "?lhc_titleName=" + linkTitleTmp
                # raw_input("press any key to continue ...")
            htmllinkdata = htmllinkdata + "\n".join(script_link_list)

            with open(strLinkListFile, 'wb') as fw:
                fw.write(htmllinkdata.encode(encoding="utf-8"))
        iTmp = iTmp + 1
        print(link_file + ":将页面链接提取到文件中,success!")
        #input("....")
    return "将页面链接提取到文件中,success!"

#该函数功能为将页面链接格式化链接为http://格式到文件中
def FormatLink(currPath,link_list_file,bmlink_list,bmlink_title_list,FileName_time,link_list_http_file):
    print("#将页面链接格式化链接为http://格式到文件中")
    iTmp = 0
    for LinkListFile in link_list_file:
        link_list = []
        with open(link_list_file[iTmp],'rb') as fr:
            for line in fr.readlines():
                #print(line.decode('utf-8'))
                link_list.append(line.decode('utf-8').strip())
            jTmp = 0
            for eachlink in link_list:
                # 处理下链接中带<img <map <area,替换为./
                if ("<img" in eachlink or "<map" in eachlink or "<area" in eachlink or "</map>" in eachlink or "javascript:" in eachlink):
                    eachlink = "./"
                link_list[jTmp] = urljoin(bmlink_list[iTmp], eachlink)
                jTmp = jTmp + 1
            strLinkListFile_http = currPath + '/jcbg/bmxxgkLinkHttpTest/' + bmlink_title_list[iTmp] + FileName_time + ".html"
            link_list_http_file.append(strLinkListFile_http)
            with open(strLinkListFile_http,'wb') as fw:
                fw.write(("\n".join(link_list)).encode(encoding="utf-8"))
        iTmp = iTmp + 1
    print("将页面链接格式化链接为http://格式到文件中,success!")
    return "将页面链接格式化链接为http://格式到文件中,success!"