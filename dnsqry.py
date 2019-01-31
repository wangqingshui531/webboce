
# -*- coding: utf-8 -*-
import dns.resolver
import os
import sys
import time

#官方文档http://www.dnspython.org/docs/1.16.0/
def dnsquery(domain=""):
    dnsQryAns = None
    try:
        dnsserver = dns.resolver.Resolver('',False)
        #当前仅支持windows
        if sys.platform == 'win32':
            dnsserver._config_win32_nameservers("221.131.143.69")
        dns.resolver.override_system_resolver(dnsserver)

        dnsQryAns=dns.resolver._resolver.query(domain,'A')
        return dnsQryAns
    except Exception as e:
        print (e)

    return
def IsJudCDNByDNSSever():
    start = time.time()
    A = dnsquery("img01.js.10086.cn")
    for i in A.response.answer:
        print(i.items)
        for j in i.items:
            print(j.address)
            if j.address == '221.178.251.146':
                return True
    runtime = (time.time() - start)*1000
    print ('查询DNS耗时[%f]ms' % runtime)
    return False

def JudSiteByHost():
    f=open("C:\Windows\System32\drivers\etc\hosts", mode='r')
    content=f.readlines()
    for i in content:
        arry = i.split(' ', 1)
        if(len(arry)==2):
            if(arry[1] == 'files01.js.10086.cn\n') and arry[0] == '39.134.69.205':
                return "standbyCDN"
            elif(arry[1] == 'files01.js.10086.cn\n') and arry[0] == '183.207.130.152':
                return "activeCDN"
    return "sourceSite"

