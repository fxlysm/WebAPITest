# -*-coding:utf-8-*-

import hashlib

def MD5sign(str,key):#传入预签名的字段与key值
    #MD5签名计算公式：
    #sign = Md5(原字符串&key=商户密钥).toUpperCase  #此句为JAVA语法
    m = hashlib.md5()
    sign = m.update(str+'&key='+key)
    # print m.hexdigest()
    return m.hexdigest()


def signstr(str):#传入预签名的字段与key值
    #MD5签名计算公式：
    #sign = Md5(原字符串&key=商户密钥).toUpperCase  #此句为JAVA语法
    m = hashlib.md5()
    sign = m.update(str)
    # print m.hexdigest()
    return m.hexdigest()


