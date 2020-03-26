# -*- coding: utf-8 -*-
# @Author  : Awaken
# @File    : config.py
# @Time    : 2020-03-26 12:30

environment = {
    'dev': "-test",
    'beta': "-test2",
    'release': ""
}
currentEnvironment = "beta"; #   当前环境
    #  domainName 域名    environment[currentEnvironment]
def urls():
    domainName = {
        'uUrl' : 'https://u-api'+environment[currentEnvironment]+'.ecpei.cn',   #   用户管理域名
        'vUrl' : 'https://v-api'+environment[currentEnvironment]+'.ecpei.cn' ,#   VIN域名
        'megUrl':'https://message-api'+environment[currentEnvironment]+'.ecpei.cn',  #   消息域名
        'iUrl':'https://i-api'+environment[currentEnvironment]+'.ecpei.cn'  #   求购域名
    }
    return domainName
# print(urls()['vUrl'])

def interfaces():
    #   interfaceName   接口名
    interfaceName = {
        "login" :   '/api/user/login'   #   登录接口

    }
    return interfaceName
