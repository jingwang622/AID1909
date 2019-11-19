"""
给进程函数传参
"""
from time import *
from multiprocessing import Process
# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")
# p = Process(target=worker,args = (2,'Baron'))
# p = Process(target=worker,kwargs={'name':'Levi','sec':3})
p = Process(target=worker,kwargs={'name':'Levi','sec':3})
p.start()
p.join()