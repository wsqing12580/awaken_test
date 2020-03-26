# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/25 20:00
# # __File__  = runtest.py
## __status__ == finish

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
        name = 'result' #   测试报告文件名尾缀
        path = './test_case/ryp_01'    #   测试脚本路径
        # path = './test_case/jike_01'

        for filename in os.listdir(self.cases):
            if filename == "test_report":
                break
        else:
            os.mkdir(self.cases + '/test_report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./test_report/" + now + name+".html", 'wb')  # 打开文件，没有自动创建
        # tests = unittest.defaultTestLoader.discover("./ryp_01", pattern='*.py', top_level_dir=None)
        tests = unittest.defaultTestLoader.discover(path, pattern='*.py', top_level_dir=None)
        # path 测试脚本路径
        # pattern   筛选测试脚本文件

        runner = HTMLTestRunner(stream=fp, title=self.tille, description=self.des)  #stream 指定测试报告文件
        runner.run(tests)
        fp.close()

    # def debug(self):
    #     tests = unittest.defaultTestLoader.discover(self.cases, pattern='*.py', top_level_dir=None)
    #     runner = unittest.TextTestRunner()
    #     runner.run(tests)

if __name__ == '__main__':
    test = TestRunner()
    test.run()

