#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
import redis
import global_setting
from conf import redis_config
class redishelper:
    def __init__(self):
        self.redis_connect=redis.Redis(**redis_config.redis_args)
        self.chan_pub='fm101'
        self.chan_sub='fm101'
    def set(self,key,value):
        self.redis_connect.set(key,value)
    def get(self,key):
        return self.redis_connect.get(key)
    def public(self,msg):
        self.redis_connect.publish(self.chan_pub,msg)
    def subscribe(self):
        pub=self.redis_connect.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
