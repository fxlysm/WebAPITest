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
    '''管理后台-商家商品管理'''
    def setUp(self):
        self.logging = HbLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.c=''
        self.userName=mgr_login_username
        # self.password=signstr(mgr_login_password)
        self.password = mgr_login_password
        self.logging.info(u"执行用例归属于>>:{}".format(self.__doc__))
        self.logging.info('Username:{}'.format(mgr_login_username))
        self.logging.info( 'Password:{}'.format(self.password) )
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : ", time.strftime('%Y-%m-%d  %H:%M:%S  %A')

    def tearDown(self):
        # self.logging.info(u"执行文件名称:{}".format(self.__module__))

        print ''
    def testshoperInsaleList(self):
        '''销售中---商品列表'''
        data = {'name':'',
                'offset':'1',
                'state':'1',
                'size':'10',
                'status':'1'}
        apiurl = mgr_shoper_insalegoods_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testshoperInsale_name_query(self):
        '''销售中---商家编号搜索'''
        data = {'name':mgr_shoper_name,
                'offset':'1',
                'state':'1',
                'size':'10',
                'status':'1'}
        apiurl = mgr_shoper_insalegoods_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)






class SuNingGoodList(unittest.TestCase):
    '''管理后台-苏宁商品管理'''
    def setUp(self):
        self.logging = HbLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.c=''
        self.userName=mgr_login_username
        # self.password=signstr(mgr_login_password)
        self.password = mgr_login_password
        self.logging.info(u"执行用例归属于>>:{}".format(self.__doc__))
        self.logging.info('Username:{}'.format(mgr_login_username))
        self.logging.info( 'Password:{}'.format(self.password) )
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : ", time.strftime('%Y-%m-%d  %H:%M:%S  %A')

    def tearDown(self):
        # self.logging.info(u"执行文件名称:{}".format(self.__module__))

        print ''

    def testInsaleList(self):
        '''销售中'''
        data = {'limit':'10','offset':'1','state':'1','productName':'','productNo':'','level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testInsaleList_oneGoodQuery1(self):
        '''销售中----某个商品编号搜索查询'''
        data = {'limit':'10','offset':'1','state':'1','productName':'','productNo':productNo_onsale,'level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testInsaleList_oneGoodQuery2(self):
        '''销售中----某个商品名搜索查询'''
        data = {'limit':'10','offset':'1','state':'1','productName':productName_onsale,'productNo':'','level':'','categoryId':''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testoffsaleList(self):
        '''已下架'''
        data = {'limit': '10', 'offset': '1', 'state': '0', 'productName': '', 'productNo': '', 'level': '',
                'categoryId': ''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)

    def testblockedsaleList(self):
        '''已屏蔽'''
        data = {'limit': '10', 'offset': '1', 'state': '2', 'productName': '', 'productNo': '', 'level': '',
                'categoryId': ''}
        apiurl = mgr_suning_Insale_pageListOfManag_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testGoodsDetails(self):
        '''某个商品的详情'''
        data = {'skuNo': skuNo_01}
        apiurl = mgr_suning_goods_details
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)


    def testGoodsShopInsale(self):
        '''上架商家查看'''
        data = {'skuNo': skuNo_02}
        apiurl = mgr_shop_goods_insale_query_url
        print MGR_Common_Query(self, self.userName, self.password, data, apiurl)



if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = "report\\" + now + 'result.html'  # 定义个报告存放路径，支持相对路径。
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    unittest.main()
