# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __uptime__ = '2020/3/25 19:10
# # __File__  = param_login.py
## __status__ == finish

"""
    Excel参数化登录，保留

"""
# from param import parafile
import unittest,common

LUrl = 'https://u-api-test2.ecpei.cn'
comm = common.Common(LUrl) # 调用common类
parafile = common.parafile  #   param.parafile获取全部参数函数
#登录页路由
uri = '/api/user/login'

class login_input():
    # 实现登录功能
    def test_login(username,password):

        payload = {
            'username': username,
            'password': password,
            'login_type': '0',
            'dev_name': 'Apple-iPhone 6 Plus',
            'imei': '0ea23ebc5fa041739e6701a1e88becb8',
            'identity_no': '1002',
            'app_type': 2
        }
        res_login = comm.post(uri, params=payload)
        return res_login.json()

class login(unittest.TestCase):
        def test_login1(self): #    正确的账户和密码
            Ldict = parafile.paraDict(r'E:\Dev\DEV1.0.2\file','/ryp_login.xls')  # 所有参数的字典
            #   E:/Dev/demo1.0.1/file
            h = 0   #   成功数
            j = 0   #   失败数
            i = 0
            while i < len(Ldict):
                # 读取通过参数类获取的第i行的参数
                username = Ldict[i]['username']  # 读取username
                password = Ldict[i]['password']
                # 读取通过参数类获取的第i行的预期
                exp = Ldict[i]['exp']

                result = login_input.test_login(username, password)
                re_meg = result['message']  #   读取message的值跟预期的值进行比较
                self.assertEqual(re_meg, exp)
                print('测试用例>>username：',username,'password：',password)
                i = i + 1
            #     try:
            #         self.assertEqual(re_meg, exp)
            #         h += 1
            #     except AssertionError as e:  # 断言语句失败
            #         #   怎么在参数化  断言错误之后继续执行后面的测试用例且可以统计到错误的用例数
            #         print('测试失败，入参username：', username, '第',i,'条测试用例','错误说明', e)
            #         j += 1
            #
            # print('测试用例数', h + j, '测试通过:', h, '测试失败', j)


if __name__ == "__main__":
      unittest.main()
#     #   构造测试套件
#     suite = unittest.TestSuite()#TestSuite 测试套件
#     suite.addTest(login("test_login1"))
#     suite.addTest(login("test_login2"))
#     suite.addTest(login("test_login3"))
#     suite.addTest(login("test_login4"))
#     suite.addTest(login("test_login5"))
#     #   执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)




