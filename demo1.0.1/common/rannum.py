# -*- coding: utf-8 -*-
# @Author  : Awaken
# @File    : rannum.py
# @Time    : 2020-03-26 19:00

import random,string

#   生成随机手机号
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),  # 随机数字0 - 9
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    phone = "1{}{}{}".format(second, third, suffix)
    # 拼接手机号
    return phone

# 打印生成手机号
# phone = create_phone()
# print(phone)

#   生成随机密码
def create_passwd(num):
    if num >8:
        passwd = set(random.sample(string.ascii_letters+string.digits,num))
        set1 = set(string.ascii_uppercase).intersection(passwd)
        set2 = set(string.ascii_lowercase).intersection(passwd)
        set3 = set(string.digits).intersection(passwd)
        if set1 and set2 and set3 :
            str_passwd=''.join(passwd) #'#要把产生的密码变成字符串，因为前面已经给变成集合了
            return str_passwd
    else:
        passwd = set(random.sample(string.ascii_letters + string.digits, num))
        str_passwd = ''.join(passwd)  # '#要把产生的密码变成字符串，因为前面已经给变成集合了
        return str_passwd


# 打印随机的密码
# pw = create_passwd(8)
# print(pw)


# num = input('请输入一个数字：').strip() #   生成num条随机密码
# pwds = set()
# if num.isdigit():
#     while len(pwds)<int(num): # 保证生成条数足够
#         passwd = set(random.sample(string.ascii_letters+string.digits,8))
#         set1 = set(string.ascii_uppercase).intersection(passwd)
#         set2 = set(string.ascii_lowercase).intersection(passwd)
#         set3 = set(string.digits).intersection(passwd)
#         if set1 and set2 and set3:
#             str_passwd=''.join(passwd)+'\n'#要把产生的密码变成字符串，因为前面已经给变成集合了
#             pwds.add(str_passwd)
#     fw =open('pwds.txt','w')
#     fw.writelines(pwds)
# else:
#     print('你输入的不是数字')



