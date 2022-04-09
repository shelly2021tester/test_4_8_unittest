#!/usr/bin/env python
# encoding: utf-8
'''
  @author: zxl
  @file: test_login.py.py
  @time: 2022/3/28 16:22
  @desc:
'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from objects.login_object import LoginPage
from config.config import driver_path,url,sheetname,system_version,photo_path
from data.data import Datas
from log.log import logger

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()

    def test_1(self):
        '''
        验证成功登录的测试用例
        '''
        value_list=Datas().read_excel(sheetname[0])
        username=value_list[0][0]
        password=value_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        #self.assertIn('个人首页', self.driver.title, "登录失败")
        self.loginpage.click_logout()
    

if __name__=='__main__':
    unittest.main()