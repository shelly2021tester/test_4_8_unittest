# -*- coding: utf-8 -*-
# Time : 2022/4/1 22:15
# Author : shelly
# File : config.py
# Desc :

import os

root_path=os.path.dirname(os.path.dirname(__file__))
# print(root_path)

url='http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html'
driver_path=root_path+r'/driver/msedgedriver.exe'
case_path=root_path+r'/test_cases'
report_path=root_path+r'/report'
log_file=root_path+r'/log/log.txt'
file_path=root_path+r'/data/test.xlsx'
system_version='1.2'