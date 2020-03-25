# -*- coding: utf-8 -*-
# # __from__ = 'https://github.com/wsqing12580/awaken_test.git'
# # __author__ = 'Awaken'
# # __mtime__ = '2020/3/24 22:00
# # __File__  = param.py

import json
import xlrd #   xlrd是读Excel的库，xlwt是写Excel的库
import os

class Param(object):
    def __init__(self,paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):   #   行扫描参数
        pass
    def paramColsCount(self):
        pass
    def paramHeader(self):  #   参数头
        pass
    def paramAllline(self): #   准直线
        pass
    def paramAlllineDict(self):
        pass

class XLS(Param):
    '''
    xls基本格式(如果要把xls中存储的数字按照文本读出来的话,纯数字前要加上英文单引号:
    第一行是参数的注释,就是每一行参数是什么
    第二行是参数名,参数名和对应模块的po页面的变量名一致
    第3~N行是参数
    最后一列是预期默认头Exp
    '''

    def __init__(self, paramConf):
        '''
        :param paramConf: xls 文件位置(绝对路径)
        '''
        self.paramConf = paramConf
        self.paramfile = self.paramConf['file']
        self.data = xlrd.open_workbook(self.paramfile)  #   打开Excel文件读取数据
        self.getParamSheet(self.paramConf['sheet']) #   #   sheet表示参数在Excel中的第几个工作表中


    def getParamSheet(self,nsheets):
        '''
        设定参数所处的sheet
        :param nsheets: 参数在第几个sheet中
        :return:
        '''
        self.paramsheet = self.data.sheets()[nsheets]

    def getOneline(self,nRow):
        '''
        返回一行数据
        :param nRow: 行数
        :return: 一行数据 []
        '''

        return self.paramsheet.row_values(nRow)

    def getOneCol(self,nCol):
        '''
        返回一列
        :param nCol: 列数
        :return: 一列数据 []
        '''
        return self.paramsheet.col_values(nCol)

    def paramRowsCount(self):
        '''
        获取参数文件行数
        :return: 参数行数 int
        '''
        return self.paramsheet.nrows

    def paramColsCount(self):
        '''
        获取参数文件列数(参数个数)
        :return: 参数文件列数(参数个数) int
        '''
        return self.paramsheet.ncols

    def paramHeader(self):
        '''
        获取参数名称
        :return: 参数名称[]
        '''
        return self.getOneline(1)   #   第一行是参数说明    第二行是参数名称

    def paramAlllineDict(self):
        '''
        获取全部参数
        :return: {{}},其中dict的key值是header的值
        '''
        nCountRows = self.paramRowsCount()  #   行数
        nCountCols = self.paramColsCount()  #   列数
        ParamAllListDict = {}

        iRowStep = 2    #   行数：从第三行开始
        iColStep = 0    #   列数：从第一列开始
        ParamHeader= self.paramHeader()

        while iRowStep < nCountRows:
            ParamOneLinelist=self.getOneline(iRowStep)
            ParamOnelineDict = {}
            while iColStep<nCountCols:
                ParamOnelineDict[ParamHeader[iColStep]]=ParamOneLinelist[iColStep]
                iColStep=iColStep+1
            iColStep=0
            #print ParamOnelineDict
            ParamAllListDict[iRowStep-2]=ParamOnelineDict
            iRowStep=iRowStep+1
        return ParamAllListDict

    def paramAllline(self):
        '''
        获取全部参数
        :return: 全部参数[[]]
        '''
        nCountRows= self.paramRowsCount()
        paramall = []
        iRowStep =2
        while iRowStep<nCountRows:
            paramall.append(self.getOneline(iRowStep))
            iRowStep=iRowStep+1
        return paramall
    def __getParamCell(self,numberRow,numberCol):
        return self.paramsheet.cell_value(numberRow,numberCol)


class ParamFactory(object):
    def chooseParam(self,type,paramConf):
        map_ = {
            'xls': XLS(paramConf)
        }
        return map_[type]


class parafile(object):
    #   parafile    返回测试用例表中的数据至searchparam_dict字典，运行测试用例执行循环字典数据
    #   需要Excel 参数化测试用例，只要导入parafile这个类就可以用

    def paraDict(path,filename,sheet=0):  #path文件路径、filename文件名、sheet工作表
        curPath = os.path.abspath(path)
        # 定义存储参数的excel文件路径
        searchparamfile = curPath + filename  # searchparamfile ：Excel文件绝对路径
        # 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
        searchparam_dict = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': sheet}).paramAlllineDict()
        #   xls ：type入参，文件类型
        #   sheet：用例在Excel的工作表位置 从0起始,默认是0
        #   paramAlllineDict    获取全部参数
        return searchparam_dict

'''
if __name__=='__main__':
    param = ParamFactory().chooseParam('xls',{'file':'searchkeyword.xls','sheet':0})
    print param.paramAlllineDict()'''