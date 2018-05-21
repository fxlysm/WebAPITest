# -*- coding: gbk -*-

'''
Created on 2017-7-24

@author: dell
'''


import sys
import telnetlib
import time
import json
import urllib2
import requests


def MallMGRLogin(userName,password):
    # username = 'admin'
    # password = '96e79218965eb72c92a549dd5a330112'
    #

    print userName
    print password
    host = 'http://sit.mall-mgr-sn.1332255.com/mall-mgr-sn-api//authentication'
    d = {'username': userName, 'password': password}
    r = requests.post(host, data=d)
    html = r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode=='200':
        token = decodejson['responseContent']['token']
        print token
    else:
        print decodejson['statusMessage']


def main():
    host = 'http://sit.mall-mgr-sn.1332255.com/mall-mgr-sn-api//authentication'
    username = 'admin'
    password = '96e79218965eb72c92a549dd5a330112'


    d = {'username': username, 'password': password}
    r = requests.post(host, data=d)
    html=r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode == '200':
        token = decodejson['responseContent']['token']
        print token
    else:
        print decodejson['statusMessage']
    # token = r.cookies.items()[0][1]
    # token2=decodejson['responseContent']['token']
    # print token
    # print html
    # print token2



if __name__ == "__main__":
    MallMGRLogin('admin','96e79218965eb72c92a549dd5a330112')
    main()