#!/usr/bin/env python2.7
from utils import global_setting
from templet import Basetemplet
client_1=Basetemplet.linuxtemplet()
client_1.host_ip='192.169.186.134'
client_2=Basetemplet.linuxtemplet()
client_3.host_ip='192.169.186.135'
client_3=Basetemplet.unixtemplet()
client_4.host_ip='192.169.186.134'
group=['192.169.186.134','192.169.186.135']
