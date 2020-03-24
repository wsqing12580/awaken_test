# -*- coding: utf-8 -*-
# # __from__ = '极客时间 - 接口测试入门'

# python代码中引入requests库，引入后才可以在你的代码中使用对应的类以及成员函数
import requests
# 建立url_login的变量，存储战场系统的登录URL
url_login = 'http://127.0.0.1:12356/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
# 调用requests类的post方法，也就是HTTP的POST请求方式，
# 访问了url_login，其中通过将payload赋值给data完成body传参
response_login = requests.post(url_login, data=payload)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_login.text)

# 断言
assert response_login.status_code == 200
