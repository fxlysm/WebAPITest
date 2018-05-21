#!/usr/bin/env python
# coding=utf-8

"""
FuncName: HbTestRunner.py
Desc: run testcases ,create report
Date: 2016-11-03 10:30
Home: http://blog.csdn.net/z_johnny
Author: johnny
"""

from HbTestReport import HTMLTestReport
from HbLogging import HbLogging
import time,os,sys
import ConfigParser
import unittest


class HbTestRunner(object):
    def __init__(self, cases_path, config_runner, config_logging,suite):
        self.cases_suite = []
        self.cases_path = cases_path
        self.suite = suite
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_runner)
        self.logging = HbLogging(config_logging).outputLog()

    def getAllCases(self):
        ''' Get all testcase '''
        # for parent,dirnames,filenames in os.walk(self.cases_path):
        #
        #     for filename in filenames:
        #         self.logging.info('文件总数 : %s'%(len(filenames)))
        #         print '文件： '+filename   #输出CAse目录下的所有文件
        #
        #         if filename.endswith('.py'):
        #             cases_list = filename.split('.py')
        #             print cases_list
        #             print os.path.join(parent, filename)
        #             self.cases_suite.append(cases_list[0])
        #             self.logging.info('The testcase name is : %s'%filename)
        #             print '%s'%filename
        # print self.cases_suite
                
        cases = os.listdir(self.cases_path)
        self.logging.info('The testcase number is : %s'%(len(cases)))
        for case in cases:
            # Split endswith and add to list
            if case.endswith('.py'):
                cases_list = case.split('.py')
                self.cases_suite.append(cases_list[0])
                self.logging.info('The testcase name is : %s'%case)
                print '%s'%case


    def runCases(self):
        ''' Run all testcase (copy it for nose) '''
        sys.path.append(self.cases_path)
        for test_case in self.cases_suite:
            try:
                print test_case.globals()
                mod = __import__(test_case.globals(),locals(),[self.suite])
                suitefn = getattr(mod,self.suite)
                print '用例'+suitefn
                self.suite.addTest(suitefn())
            except (ImportError,AttributeError):
                self.suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_case))

    def addReport(self):
        ''' Collect all testcase result to HTMLTestRunner'''
        report_name = self.config.get("report","name").decode("UTF-8")
        now=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
        localtime = str(time.strftime('%Y_%m_%d_%A_%H_%M_%S'))
#         filename = './report/%s%s.html'%(report_name,localtime)
        filename = './report/%s%s.html'%(report_name,now)

        with open(filename, 'wb') as report:
            runner = HTMLTestReport(stream=report,
                                    title=self.config.get("report","title").decode("UTF-8"),
                                    description=self.config.get("report","description").decode("UTF-8"),
                                    tester=self.config.get("report","tester").decode("UTF-8"))
            runner.run(self.suite)
    def run(self):
        self.getAllCases()
        self.runCases()
        self.addReport()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases_path = "./cases"
    config_runner = './config/reportConfig.ini'
    config_logging = './config/logConfig.ini'
    test = HbTestRunner(cases_path,config_runner,config_logging,suite)
    test.run()
