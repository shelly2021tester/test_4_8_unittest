# -*- coding: utf-8 -*-
# Time : 2022/4/1 21:11
# Author : shelly
# File : atest_page2.py
# Desc :
import unittest


class UserCases(unittest.TestCase):
    # testfixture
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')

    def test_1(self):
        print('用户的第一个测试用例')

    def test_2(self):
        print('用户第二个测试用例')