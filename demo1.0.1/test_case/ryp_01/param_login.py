# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/demo.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = param_login.py

from common import Common
from param import ParamFactory
import unittest,os,json,requests

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
            #   读取文件参数
            curPath = os.path.abspath(r'E:\Dev\demo1.0.1\file')
            # 定义存储参数的excel文件路径
            searchparamfile = curPath + '/ryp_login.xls'  # searchparamfile ：Excel文件绝对路径
            # 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
            searchparam_dict = ParamFactory().chooseParam('xls',
                                                          {'file': searchparamfile, 'sheet': 0}).paramAlllineDict()
            #   xls ：type入参，文件类型
            #   sheet：用例在Excel的工作表位置
            #   paramAlllineDict    获取全部参数

            i = 0
            while i < len(searchparam_dict):
                # 读取通过参数类获取的第i行的参数
                username = searchparam_dict[i]['username']  # 读取username
                password = searchparam_dict[i]['password']
                # 读取通过参数类获取的第i行的预期
                exp = searchparam_dict[i]['exp']

                lo = login_input.test_login(username, password)
                print('运行结果',lo)
                result = lo['message']
                # print(i,'登录返回json：', lo)
                # uid = lo['data']['uid']
                # token = lo['data']['token']
                # return uid,token
                self.assertEqual(result, exp)
                # print('运行message：',result)
                # print('username=',username,'password',password)
                i = i + 1
                print('测试用例数：',i)


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




