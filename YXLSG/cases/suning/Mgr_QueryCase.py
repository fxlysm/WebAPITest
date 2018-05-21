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

class ShoperGoodList(unittest.TestCase):
    '''�����̨-�̼���Ʒ����'''
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
    def testshoperInsaleList(self):
        '''������---��Ʒ�б�'''
        data = {'name':'',
                'offset':'1',
                'state':'1',
                'size':'10',
                'status':'1'}
        apiurl = mgr_shoper_insalegoods_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testshoperInsale_name_query(self):
        '''������---�̼ұ������'''
        data = {'name':mgr_shoper_name,
                'offset':'1',
                'state':'1',
                'size':'10',
                'status':'1'}
        apiurl = mgr_shoper_insalegoods_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)






class SuNingGoodList(unittest.TestCase):
    '''�����̨-������Ʒ����'''
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

    def testInsaleList(self):
        '''������'''
        data = {'limit':'10','offset':'1','state':'1','productName':'','productNo':'','level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testInsaleList_oneGoodQuery1(self):
        '''������----ĳ����Ʒ���������ѯ'''
        data = {'limit':'10','offset':'1','state':'1','productName':'','productNo':productNo_onsale,'level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testInsaleList_oneGoodQuery2(self):
        '''������----ĳ����Ʒ��������ѯ'''
        data = {'limit':'10','offset':'1','state':'1','productName':productName_onsale,'productNo':'','level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testoffsaleList(self):
        '''���¼�'''
        data = {'limit': '10', 'offset': '1', 'state': '0', 'productName': '', 'productNo': '', 'level': '',
                'categoryId': ''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testblockedsaleList(self):
        '''������'''
        data = {'limit': '10', 'offset': '1', 'state': '2', 'productName': '', 'productNo': '', 'level': '',
                'categoryId': ''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testGoodsDetails(self):
        '''ĳ����Ʒ������'''
        data = {'skuNo': skuNo_01}
        apiurl = mgr_suning_goods_details
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testGoodsShopInsale(self):
        '''�ϼ��̼Ҳ鿴'''
        data = {'skuNo': skuNo_02}
        apiurl = mgr_shop_goods_insale_query_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)



if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = "report\\" + now + 'result.html'  # �����������·����֧�����·����
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    unittest.main()
