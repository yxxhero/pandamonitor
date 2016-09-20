#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
class basetemplet(object):
    def __init__(self):
        self.host_ip=''
        self.group=''
class linuxtemplet(basetemplet):
    def __init__(self):
        super(linuxtemplet,self).__init__()
        self.server=['mem_infomation']
        self.name='linux'
        self.mem_info_interval=10
        self.cpu_info_interval=20
class unixtemplet(basetemplet):
    def __init__(self):
        super(unixtemplet,self).__init__()
        self.server=['cpu_infomation']
        self.name='unix'
        self.mem_info_interval=10
        self.cpu_info_interval=20
