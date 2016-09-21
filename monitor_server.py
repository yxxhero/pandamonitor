#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
from utils import global_setting
from templet import Basetemplet
from utils import redishelper
import time
import pickle
import threading
def save_data_to_redis(m_data,redis_ins):
    current_time=time.time()
    monitor_ip=m_data.keys()[0]
    print monitor_ip
    redis_data=m_data.keys()[0]+':'+str(current_time)
    redis_ins.set(redis_data,pickle.dumps(m_data[monitor_ip]))
    print "save ok"
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
    monitor_data=pickle.loads(monitor_result[2])
    t=threading.Thread(target=save_data_to_redis,args=(monitor_data,r))
    t.start() 

