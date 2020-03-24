# -*- coding: utf-8 -*-

#引入Common、ParamFactory类
from common import Common
from param import ParamFactory
import os,json

# uri_login存储战场的选择武器
uri_selectEq = '/selectEq'
comm = Common('http://127.0.0.1:12356')
# 武器编号变量存储武器编号，并且验证返回时是否有参数设计预期结果
# 获取当前路径绝对值
curPath = os.path.abspath(r'E:\Dev\demo1.0.1\file')
# 定义存储参数的excel文件路径
searchparamfile = curPath+'/selectEq.xls'   #   searchparamfile ：Excel文件绝对路径
# 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
searchparam_dict = ParamFactory().chooseParam('xls',{'file':searchparamfile,'sheet':0}).paramAlllineDict()
    #   xls ：type入参，文件类型
    #   sheet：用例在Excel的工作表位置
    #   paramAlllineDict    获取全部参数
i=0
a = 0  # 成功数
b = 0  # 失败数
while i<len(searchparam_dict):
  # 读取通过参数类获取的第i行的参数
  payload = 'equipmentid=' + searchparam_dict[i]['equipmentid']
  # 读取通过参数类获取的第i行的预期
  exp=searchparam_dict[i]['exp']
  # 进行接口测试
  response_selectEq = comm.post(uri_selectEq,params=payload)
  # 打印返回结果

  re = json.dumps(response_selectEq.json()['Message'])

  print('Response内容：' + re)
  if exp in re:
      print('测试通过！Message预期结果:',exp,' 实际结果：',re)
      a = a + 1
  else:
      print('测试失败！Message预期结果:',exp,' 实际结果：',re)
      b += 1
  # print('Response内容：' + response_selectEq.text)
  # # 读取下一行excel中的数据
  i=i+1

print('测试用例数',a+b,'测试通过:',a,'测试失败',b)