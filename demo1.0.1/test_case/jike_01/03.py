# -*- coding: utf-8 -*-
# # __from__ = '极客时间 - 接口测试入门'

# Python代码中引入requests库，引入后才可以在你的代码中使用对应的类以及成员函数
from common import Common
IPUrl = 'http://127.0.0.1:12356'

# 首页的路由
uri = '/'
# 实例化自己的Common
comm = Common(IPUrl)
#调用你自己在Common封装的get方法 ，返回结果存到了response_index中
response_index = comm.get(uri)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)
print('url=',response_index.url)