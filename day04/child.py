"""
模拟二级子进程
"""
from time import sleep
import os
import sys
def foo():
    sleep(3)
    print("模拟事件foo")
def bar():
    sleep(5)
    print("模拟时间bar")

p1 = os.fork()  # 创建一级子进程
if p1 == 0:
    p2 = os.fork()
    if p2 == 0:
        # 二级子进程
        foo()
    else:
        os._exit(0)

else:
    os.wait()
    bar()

