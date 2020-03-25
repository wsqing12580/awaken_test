# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = test_login.py

"""
    在测试步骤中写死接口入参，保留
"""

from common import Common
import unittest

LUrl = 'https://u-api-test2.ecpei.cn'
comm = Common(LUrl) # 调用common类
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
        lo = login_input.test_login('17665486286','111111')
        result = lo['message']
        print('成功登录 1 json：',lo)
        # print('uid = ',lo['data']['uid'])
        # print('token = ',lo['data']['token'])
        # uid = lo['data']['uid']
        # token = lo['data']['token']
        # return uid,token
        self.assertEqual(result,'success')
        # self.assertEqual(result, '账号或密码错误')

    def test_login2(self): #    账号或密码错误
        lo = login_input.test_login('17665486286','112131111')
        result = lo['message']
        print('登录2 json :',lo)

        # print(result)
        self.assertEqual(result, '账号或密码错误')

    def test_login3(self):  # 不存在的账号登录
        lo = login_input.test_login('1545786565','454545')
        result = lo['message']
        print('登录3 json :',lo)
        self.assertEqual(result, '账号不存在')


    def test_login4(self):  # 不输入账号登录
        lo = login_input.test_login('','121122112')
        result = lo['message']
        print('登录4 json :',lo)
        self.assertEqual(result, '手机号码不能为空')

    def test_login5(self):  # 不输入密码登录
        lo = login_input.test_login('17665486286','')
        result = lo['message']
        print('登录5 json :',lo)
        self.assertEqual(result, '密码不能为空')
#
if __name__ == "__main__":
    unittest.main()


# if __name__ == "__main__":
#     #   unittest.main()
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

# if __name__ == "__main__":
#     # 可以把要执行的测试用例用个列表来管理，然后再把这个列表添加到测试套件中
#     #   构造测试套件
#     suite = unittest.TestSuite()#TestSuite 测试套件
#     test_cases  = [login("test_login5")]
#
#     suite.addTests(test_cases)
#     #   执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


