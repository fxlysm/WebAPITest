# -*- coding: gbk -*-
from src.HbLogging import *
from mode.suning.mgr_login import *
from config.suning.mall_mgr_config import *
import sys
from src.HTMLTestRunner import *
import  demjson
import Cookie
import unittest,time,urllib,urllib2
from mode.SignUtil import *
reload(sys)

class MallLogInTestCase(unittest.TestCase):
    '''������̨-��¼��ע��'''
    def setUp(self):
        self.logging = HbLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.c=''
        self.userName=mgr_login_username
        # self.password=signstr(mgr_login_password)
        self.password = mgr_login_password
        self.logging.info(u"ִ������������>>:{}".format(self.__doc__))
        self.logging.info('Username:{}'.format(mgr_login_username))
        self.logging.info( 'Password:{}'.format(self.password) )
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : ", time.strftime('%Y-%m-%d  %H:%M:%S  %A')

    def tearDown(self):
        # self.logging.info(u"ִ���ļ�����:{}".format(self.__module__))

        print ''


    def testmgrlogin(self):
        '''������̨-��¼'''
        print MallMGRLogin(self,self.userName,self.password)

    def testGettodayRealTimeData(self):
        '''�̳ǹ�����̨-��ȡ��ҳ-����ʵʱ'''
        data = {}
        apiurl=mgr_shopinfo_url
        print MGR_Common_Query(self,self.userName,self.password,data,apiurl)

    def testGetshopGeneralSituation(self):
        '''������̨-��ȡ��ҳ-����״̬'''
        data = {}
        apiurl=mgr_shopGeneralSituation_url
        print MGR_Common_Query(self,self.userName,self.password,data,apiurl)

    def testGetcommonFunctions(self):
        '''������̨-��ȡ��ҳ-���ù���'''
        data = {}
        apiurl=mgr_commonFunctions_url
        print MGR_Common_Query(self,self.userName,self.password,data,apiurl)


    def testmgrlogout(self):
        '''������̨ע��'''
        print ''



if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = "report\\" + now + 'result.html'  # �����������·����֧�����·����
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    unittest.main()