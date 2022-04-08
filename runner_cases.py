# -*- coding: utf-8 -*-
# Time : 2022/4/1 21:13
# Author : shelly
# File : runner_cases.py
# Desc :

import unittest
from BeautifulReport import BeautifulReport
from config.config import case_path,report_path

#加载批量的测试用例
suite=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')
# runner=unittest.TextTestRunner()
# runner.run(suite)
result=BeautifulReport(suite)
result.report(description='系统登录的测试报告',filename='SIT测试报告',report_dir=report_path)