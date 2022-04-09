from BeautifulReport import BeautifulReport
import unittest
from config.config import cases_path,report_path


cases = unittest.defaultTestLoader.discover(start_dir=cases_path,\
                                          pattern = 'test*.py')
result = BeautifulReport(cases)
result.report(description='登录的测试报告',filename='第一轮测试结果',
              report_dir=report_path)
