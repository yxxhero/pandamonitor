#!/use/bin/env python2.7
#_*_ coding:utf-8 _*_
from utils import global_setting
from plugins import get_system_info
from utils import redishelper
import pickle
import time
import threading
r=redishelper.redishelper()
def hanle_data(server,data):
    date_pre=data+time.time()
    pass
monitor_server=r.get("monitor_config:192.168.18.133")
server_list=pickle.loads(monitor_server)
print server_list
server_last_time={}
for i in server_list:
    server_last_time[i]=0
while True:
    for server in server_list:
        if hasattr(get_system_info,server):
            server_class=getattr(get_system_info,server)
            s=server_class()
            if time.time() - server_last_time[server] > s.interval:
                #data=server().get_info()
                #t=threading.Thread(target=handle,args=(server,data))
                print "it is time to",server
                server_last_time[server]=time.time()
            else:
                print "waitting......"
                time.sleep(1)

