# -*- coding: utf-8 -*-
# @Author  : Awaken
# @File    : test_mysql.py
# @Time    : 2020-03-26 19:00

import pymysql

import common.rannum
# phone = common.rannum.create_phone()    #   随机手机号
# passwd = common.rannum.create_passwd(8) #   随机8位密码
#   pymysql.connect 连接数据库

# mysql_conf = {
#     'host':'127.0.0.1',
#     'port': 3306,
#     'user' : 'test',
#     'passwd':111111,
#     'db':'test',
#     'cursorclass':'pymysql.cursors.DictCursor'
# }

conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'test',passwd='111111',db='test',cursorclass=pymysql.cursors.DictCursor)
    #db：库名   cursorclass=pymysql.cursors.DictCursor 查询到的数据以字典的形式输出  cursorclass –要使用的自定义光标类

try:

    for i in range(1):
         # with 用于流程控制
        with conn.cursor() as cur:  #创建游标 conn.cursor()
        #     # Create a new record
            username = common.rannum.create_phone()  # 随机手机号
            password = common.rannum.create_passwd(8) #   随机8位密码
            sql = "INSERT INTO `user_users` (`username`, `password`) VALUES (%s, %s)"   #   输入数据
            cur.execute(sql,(username,password))   # ---两种sql形式都可以，第一种可以防范SQL注入
        #     sql = "INSERT INTO user_users (username, password) VALUES ('11111111112','123456789')"
        #     cur.execute(sql)
        # # connection is not autocommit by default. So you must commit to save your changes. 翻译为：默认情况下，连接不是自动提交。所以你必须承诺保存你的更改。
            conn.commit() # # 提交

    # with conn.cursor() as cur:
    #     sql = "UPDATE `user_users` SET `password`='111111' WHERE `username`=username"
    with conn.cursor() as cur:  #创建游标 conn.cursor()
        # Read a single record
        sql = "select * from user_users where status = (%s)"
        cur.execute(sql,(0))    #   .execute执行sql
        result = cur.fetchall()  #   fetchall所有数据、fetchone()一条数据   fetchmany(3) 显示前3条数据
        print(result)
        i = 0
        List = []
        while i < len(result):
            List.append(result[i]['username'])
            i += 1
        print('username:',List)
        a = '17665486285'
        if a in List:
            print('数据库有这条数据')
        else:
            print('数据库没有这条数据')
    #
    # with conn.cursor() as cur:
    #     sql = "DELETE FROM `user_users` WHERE id <100 "
    #     cur.execute(sql)
    #     conn.commit()
    #     print('删除了数据')

finally:    #   无论怎么都会执行finally下的语句

    cur.close() # #关闭指针对象
    conn.close()    # #关闭连接对象