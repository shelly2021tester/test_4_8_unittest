#!/usr/bin/env python
# encoding: utf-8
"""
    @author: zxl
    @file: config.py
    @time: 2022/3/4 8:31
    @desc:web配置
"""
import os
path = os.path.dirname(os.path.dirname(__file__))
driver_path1=path+r'/driver/msedgedriver.exe'
driver_path=path+r"/driver/chromedriver.exe"
# url ='http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html'
url='http://iwebsns.pansaifei.com/index.php'
cases_path = path+r'/testcases'
report_path=path+r'/result'
log_path=path+r'/log/log.txt'
data_file=path+r'/data/data.xlsx'
sheetname=('login','users','buglist') #login模块表
system_version='v1.2'
photo_path=path+r'/data/others/test.jpg'