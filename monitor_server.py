#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
from utils import global_setting
from templet import Basetemplet
#from utils import redishelper
import time
client_1=Basetemplet.linuxtemplet()
client_1.host_ip='192.169.186.134'
client_2=Basetemplet.linuxtemplet()
client_2.host_ip='192.169.186.135'
client_3=Basetemplet.unixtemplet()
client_3.host_ip='192.169.186.134'
group=['192.169.186.134','192.169.186.135']
client_group=[client_1,client_2,client_3]
for ip in group:
    client_config=ip+':monitor_config'
    server_list=[] 
    for client in client_group:
        if ip==client.host_ip:
            server_list.append(client.server)
    print server_list[:]



