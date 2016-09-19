#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
class basetemplet(object):
    def __init__(self):
        self.host_ip=''
        self.group=''
class linuxtemplet(basetemplet):
    def __init__(self):
        super(linuxtemplet,self).__init__()
        self.server=['mem_info']
        self.name='linux'
class unixtemplet(basetemplet):
    def __init__(self):
        super(unixtemplet,self).__init__()
        self.server=['cpu_info']
        self.name='unix'
