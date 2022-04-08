# -*- coding: utf-8 -*-
# Time : 2022/4/1 21:11
# Author : shelly
# File : test_page1.py
# Desc :

import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from time import sleep
from selenium.webdriver.support.select import Select
from objectpage.login_page import LoginPage
from config.config import url,driver_path,system_version
from data.data import ReadWrite
from log.log import loggers

class LoginCases(unittest.TestCase):
    #testfixture
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()

    def test_1(self):
        '''
        验证有效地用户名和密码成功登录系统
        '''
        print('登录的第一个测试用例')
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(0.5)
        self.loginpage.click_logout()
        loggers.info('有效的用户名和密码成功登录系统')

