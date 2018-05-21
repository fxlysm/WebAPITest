# -*- coding: gbk -*-

import cookielib
import json
import urllib2,urllib
import requests
from config.suning.mall_mgr_config import *






def MallMGRLogin(self,username,password):

    login_path = mgr_host_url+mgr_mall_login_url
    print login_path
    print username
    print password
    d = {'userName': username, 'password': password}
    r = requests.post(login_path, data=d)
    html = r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode=='200':
        token = decodejson['responseContent']['token']
        print token
    else:
        print decodejson['statusMessage']



#共公查询
def MGR_Common_Query(self,username,password,data,apiurl):
    login_path = mgr_host_url + mgr_mall_login_url
    print login_path
    print username
    print password
    d = {'userName': username, 'password': password}
    r = requests.post(login_path, data=d)
    html = r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode == '200':
        token = decodejson['responseContent']['token']
        print token

        aa= requests.get(login_path)
        print aa
        cookies = aa.cookies
        print 'cookies:{}'.format(cookies)
        headers = {
            "Authorization": token,
            "Host": host,
            "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "cookie": cookies
        }
        shopGeneralSituation_url=mgr_host_url +apiurl
        print u'接口URL:{}'.format(shopGeneralSituation_url)
        s = requests.post(shopGeneralSituation_url, data, headers=headers)
        # 打印返回结果
        html2=s.text
        print html2
        decodejson2 = json.loads(html2)
        statusCode = decodejson2['statusCode']
        if statusCode == '200':
            print(s.status_code, s.text)
            assert True
        else:
            assert False


    else:
        print decodejson['statusMessage']



