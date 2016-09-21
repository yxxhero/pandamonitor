#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
from utils import global_setting
from templet import Basetemplet
from utils import redishelper
import time
import pickle
client_1=Basetemplet.linuxtemplet()
client_1.host_ip='192.168.86.135'
client_2=Basetemplet.linuxtemplet()
client_2.host_ip='192.168.86.136'
client_3=Basetemplet.unixtemplet()
client_3.host_ip='192.168.86.135'
group=['192.168.86.136','192.168.86.135']
client_group=[client_1,client_2,client_3]
for ip in group:
    client_config='monitor_config:'+ip
    server_list=[] 
    for client in client_group:
        if ip==client.host_ip:
            server_list.extend(client.server)
    config=pickle.dumps(server_list)
    r=redishelper.redishelper()
    r.set(client_config,config)
pub=r.subscribe()
while True:
    monitor_result=pub.parse_response()
    print pickle.loads(monitor_result[2])


