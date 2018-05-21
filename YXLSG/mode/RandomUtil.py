# -*- coding: utf-8 -*-
import random
import socket
import sys
sys_encoding = sys.getfilesystemencoding()
def getRandomStr(self,length):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def getRandomNum(self,length):
    seed = "1234567890"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def getRandomsymbol(self,length):
    seed = '~!@#$%^&*()_+-=;:,<.>/?'
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def getIP(self):
    ip='192.168'
    for i in range(2):
        ipstr=str(getRandomStr(self,2))
        print ipstr
        ip = ip + '.' +ipstr
    return ip






def printcn(msg):
    print(msg.decode('utf-8').encode(sys_encoding))

if __name__ == "__main__":
    # 兼容中文字符打印
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print sys.getdefaultencoding()
    print "我们".decode('utf-8').encode('utf-8')
    printcn("测试一下")

