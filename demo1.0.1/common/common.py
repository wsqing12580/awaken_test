# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = common.py

import requests

# 定义一个common的类，它的父类是object
class Common(object):
  # common的构造函数
  def __init__(self,url_root):
    # 被测系统的根路由
    self.url_root = url_root # 调用Common类时加上根路由，例：comm = Common('http://127.0.0.1:12356')
    # print('导入common成功')
  # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空


  def get(self, uri, params='',headers=''):
    # 拼凑访问地址
    url = self.url_root + uri + params
    # 通过get请求访问对应地址
    if len(headers) > 0:
        res = requests.get(url,headers=headers,timeout=8)
    else:
        res = requests.get(url,timeout=8)#  timeout   参数设定的时间之后停止等待响应，不使用程序可能会永远失去响应
        # 返回request的Response结果，类型为requests的Response类型
    return res

  # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
  def post(self, uri, params='',headers=''):
    # 拼凑访问地址
    url = self.url_root + uri
    if len(params) > 0:
        if len(headers) > 0:
            res = requests.post(url, data=params,headers=headers,timeout=8)
      # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
      # 返回request的Response结果，类型为requests的Response类型
        else:
          res = requests.post(url, data=params,timeout=8)
    else:
        if  len(headers) > 0:
            res = requests.get(url, headers=headers, timeout=8)
        else:
      # 如果无参数，访问方式如下
      # 返回request的Response结果，类型为requests的Response类型
          res = requests.post(url,timeout=8)
    return res

  def put(self, uri, headers='', params=None):
      '''
      封装你自己的put方法，uri是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
      :param uri: 访问路由
      :param params: 传递参数，string类型，默认为None
      :return: 此次访问的response
      '''
      url = self.url_root + uri
      if params is not None:
          if len(headers) > 0:
              # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
              # 返回request的Response结果，类型为requests的Response类型
              res = requests.put(url, headers = headers ,data=params,timeout=8)
          else:
              res = requests.put(url,data=params, timeout=8)
      else:
          if len(headers) > 0:
              res = requests.put(url, headers=headers, timeout=8)
          # 如果无参数，访问方式如下
          # 返回request的Response结果，类型为requests的Response类型
          else:
            res = requests.put(url,timeout=8)
      return res

  def delete(self, uri, headers='',params=None):
      '''
      封装你自己的delete方法，uri是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
      :param uri: 访问路由
      :param params: 传递参数，string类型，默认为None
      :return: 此次访问的response
      '''
      url = self.url_root + uri
      if params is not None:
          if len(headers) > 0:
              res = requests.delete(url, headers=headers,data=params, timeout=8)
          # 如果有参数，那么通过delete方式访问对应的url，并将参数赋值给requests.delete默认参数data
          # 返回request的Response结果，类型为requests的Response类型
          else:
            res = requests.delete(url, data=params,timeout=8)
      else:
          if len(headers) > 0:
              res = requests.delete(url, headers=headers, timeout=8)
          else:
              # 如果无参数，访问方式如下
              # 返回request的Response结果，类型为requests的Response类型
              res = requests.delete(url,timeout=8)
      return res

