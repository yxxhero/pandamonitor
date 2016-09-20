#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
import commands
class cpu_infomation:
    def __init__(self):
        self.cpu_info={}
        self.plugin_name='cpu_info'
        self.interval=30
        self.host_ip=''
    def get_info(self):
        cpu_result=commands.getoutput("top -bi -n 2|grep Cpu|grep -o '[[:space:]].*$'|awk 'NR==2{print}'").strip('\n').split(',')
        for item in cpu_result:
            self.cpu_info[item.strip().split()[1]]=item.strip().split()[0]
        return self.cpu_info
        
class mem_info:
    def __init__(self):
        self.mem_info={}
        self.plugin_name='mem_info'
        self.interval=20
        self.host_ip=''
    def get_info(self):
        with open('/proc/meminfo','r') as fd:
            for lines in fd.readlines():
                if lines.strip('\n').split(':')[0] in ['MemTotal','MemFree','Buffers','Cached','MemAvailable']:
                    self.mem_info[lines.strip('\n').split(':')[0]]=lines.strip('\n').split(':')[1].strip()
            return self.mem_info
    
