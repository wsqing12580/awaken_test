# -*- coding: utf-8 -*-
# # __from__ = '极客时间 - 接口测试入门'

import common
#登录页路由
uri = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password

comm = common.Common('http://127.0.0.1:12356')
response_login = comm.post(uri,params=payload)
print('Response内容：' + response_login.text)
print('URL = ',response_login.url)