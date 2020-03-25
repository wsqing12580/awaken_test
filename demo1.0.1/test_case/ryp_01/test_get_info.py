# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = test_get_info.py
"""
    本文件采用globals()函数存储上一接口数据给下一接口利用,已完成，保留
"""

from common import Common
import unittest

UUrl = 'https://u-api-test2.ecpei.cn'
comm = Common(UUrl) # 调用common类

Luri = '/api/user/login'    #   登录接口名
Gurl = '/api/identity/base/get_base_info?'  #  获取基本信息接口名
Curl = '/api/identity/check_join?'  #   检测是否入驻

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
    res_login = comm.post(Luri, params=payload)
    return res_login.json()

class login(unittest.TestCase): #   调用登录
    # class login(unittest.TestCase):  # 调用登录
    #     def setUp(self):  # setUp是在测试函数调用前先执行
    #         self.d = globals()
    #         #   globals()函数会已字典类型返回当前位置的全部全局变量，可用于存储上一接口数据给下一接口作为入参使用

    def test_a(self):  #   登录获取uid、token等信息
        re = test_login('17665486286', '111111')

        re_uid = re['data']['uid']  # 登录返回的uid
        re_token = re['data']['token']
        globals()['uid'] = re_uid  # uid赋值给globals字典key = uid
        globals()['token'] = re_token

        print('登录成功，uid = ',re_uid,'token = ',re_token)

        result = re['message']
        self.assertEqual(result, 'success') #   断言登录成功
    def test_b(self): # 获取基本信息
        uid = globals()['uid']   #   使用登录接口的uid
        token = globals()['token']    #    使用登录接口的token
        params = 'uid=' + uid + '&token=' + token
        get_in = comm.get(Gurl,params=params)
        print('获取到的基本信息：',get_in.json())
        print('url = ',get_in.url)


if __name__ == '__main__':
    unittest.main()