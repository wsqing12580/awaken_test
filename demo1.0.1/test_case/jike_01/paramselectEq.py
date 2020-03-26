# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/25  18:30
# # __File__  = paramselectEq.py
# # __status__  = finish

    #   参数化测试用例
#引入Common、parafile类
from param import parafile
import json,unittest,common,time

comm= common.Common('http://127.0.0.1:12356')
uri_selectEq = '/selectEq'

class strdate(unittest.TestCase):
    def test_str(self):
        a = parafile.paraDict(r'E:/Dev/demo1.0.1/file', '/selectEq.xls')  # 所有参数的字典
        h = 0   #成功数
        j = 0   #失败数
        i = 0
        while i <len(a):
            str1 = a[i]["equipmentid"]
            exp = a[i]["exp"]
            payload = 'equipmentid='+str1
            response_selectEq = comm.post(uri_selectEq, params=payload)
            re = json.dumps(response_selectEq.json()['Message'])
            i = i + 1
            # print('Response内容：' + re)
            self.assertIn(exp, re)
        #     try:
        #         self.assertIn(exp, re)
        #         h += 1
        #     except AssertionError as e: #   断言语句失败
        #         #   怎么在参数化  断言错误之后继续执行后面的测试用例且可以统计到错误的用例数
        #         print('测试失败，入参equipmentid：',str1,'错误说明',e)
        #         j += 1
        #
        # print('测试用例数', h + j, '测试通过:', h, '测试失败', j)


if __name__ == '__main__':
    unittest.main()

