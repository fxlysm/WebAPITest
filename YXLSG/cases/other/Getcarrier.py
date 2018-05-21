# -*- coding: gbk -*-
import sys
import urllib,urllib2
if sys.getdefaultencoding()!='gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')


url='https://tcc.taobao.com/cc/json/mobile_tel_segment.htm'
textmod ={'tel':'13538189575'}
textmod = urllib.urlencode(textmod)
print(textmod)
#输出内容:password=admin&user=admin
req = urllib2.Request(url = '%s%s%s' % (url,'?',textmod))
res = urllib2.urlopen(req)
res = res.read()
print res.encode('gbk', 'ignore').decode('utf-8')
#输出内容:登录成功