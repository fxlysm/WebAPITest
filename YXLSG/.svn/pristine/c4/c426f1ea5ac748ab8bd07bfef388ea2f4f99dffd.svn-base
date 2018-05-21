#!/usr/bin/env python
# coding=utf-8

'''
FuncName: startup.py
Desc: boot
Date: 2016-11-05 08:30
Author: lambert
'''
from src.HbTestRunner import HbTestRunner
from src.HbClean import HbClean
from src.HbSendEmail import HbSendEmail
import unittest
import os
import time




if __name__ == '__main__':
    suite = unittest.TestSuite()

    ISOTIMEFORMAT='_%Y-%m-%d_%A'
    current_time =str(time.strftime(ISOTIMEFORMAT))
    cases_path = "./cases/other"
    config_email= './config/emailConfig.ini'     # config path
    config_runner = './config/reportConfig.ini'
    config_logging = './config/logConfig.ini'
    pyc_path = os.getcwd()
    email_attachment_path = './report'                   # attachment path
    email_tiltle = '聚合支付业务后台&商户后台&代理商业务后台系统测试报告-'+'%s'%current_time       # as johnny test_2016-06-20_Monday ,it can choose only file when add time
    email_content = u'本轮自动化测试完成，详情请查看附件，本邮件是程序自动发送，请勿回复！---Python自动化测试报告示例 '

    testreport = HbTestRunner(cases_path,config_runner,config_logging,suite)
    testreport.run()   # same as under
    """
    testreport.getAllCases()
    testreport.runCases()
    testreport.addReport()
    """

    cleanpyc = HbClean(pyc_path)
    cleanpyc.cleanPyc()
    """
    """
    # myemail = HbSendEmail(config_email,email_attachment_path)
    # myemail.connect()
    # myemail.login()
    # myemail.send(email_tiltle, email_content)
    # myemail.quit()
    #
    # myemail =HbSendEmail(config_email, email_attachment_path)
    # myemail.sendemail(email_tiltle, email_content)





