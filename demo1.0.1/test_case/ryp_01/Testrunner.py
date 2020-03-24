# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/demo.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = Testrunner.py

import time,os,unittest
from HTMLTestRunner_cn import HTMLTestRunner

#   生成HTML测试报告

class TestRunner(object):
    "   Run test  "
    def __init__(self,cases="../",title=u'登录自动化测试报告',description=u'用例执行情况'):
        self.cases = cases
        self.tille = title  #   定义测试报告的标题
        self.des =  description #   定义测试报告的副标题

    def run(self):

        for filename in os.listdir(self.cases):
            if filename == "test_report":
                break
        else:
            os.mkdir(self.cases + '/test_report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("../../test_report/" + now + "login_result.html", 'wb')  # 打开文件，没有自动创建
        tests = unittest.defaultTestLoader.discover("./", pattern='*.py', top_level_dir=None)

        runner = HTMLTestRunner(stream=fp, title=self.tille, description=self.des)  #stream 指定测试报告文件

        runner.run(tests)
        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='*.py', top_level_dir=None)
        runner = unittest.TextTestRunner()
        runner.run(tests)

if __name__ == '__main__':
    test = TestRunner()
    test.run()


# class test_equal(unittest.TestCase):
#     def test_equal1(self): #  判断a和b是否相等
#         a = 1
#         b = 2
#         self.assertEqual(a, b)
#
# if __name__ == "__main__":
#     #   构造测试套件
#     suite = unittest.TestSuite()
#     test_cases  = [test_equal("test_equal1")]
#     suite.addTests(test_cases)
#     #   执行测试
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

