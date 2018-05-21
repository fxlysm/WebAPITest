

import cookielib
import json
import urllib2,urllib
from config.suning.buyerConf import *


def MallMLogin(self,userName,password):
    c = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
    login_path = host_url+mall_login_url
    data = {'userName': userName, 'password': password}
    post_info = urllib.urlencode(data)
    request = urllib2.Request(login_path, post_info)
    html = opener.open(request).read()
    print html.decode('utf-8').encode('gbk')
    decodejson = json.loads(html)
    resultstr = decodejson["result"]
    msgstr= decodejson[u"msg"]
    # username = decodejson[u"value"][u'userName'].decode('utf-8').encode('gbk')
    print resultstr
    print msgstr
    # print username
    return c
    if c:
        print c
    if (msg==msgstr and result== resultstr):
        assert true
    else:
        assert False



def MallMGRLogin(self,userName,password):
    c = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
    login_path = host_url+mall_login_url
    data = {'username': userName, 'password': password}
    post_info = urllib.urlencode(data)
    request = urllib2.Request(login_path, post_info)
    html = opener.open(request).read()
    print html.decode('utf-8').encode('gbk')
    decodejson = json.loads(html)
    resultstr = decodejson["result"]
    msgstr= decodejson[u"msg"]
    # username = decodejson[u"value"][u'userName'].decode('utf-8').encode('gbk')
    print resultstr
    print msgstr
    # print username
    return c
    if c:
        print c
    if (msg==msgstr and result== resultstr):
        assert true
    else:
        assert False