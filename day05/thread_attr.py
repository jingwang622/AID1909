from time import *
from threading import Thread
def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "H")
# 主线程退出分支线程也退出
t.setDaemon(True)
t.start()

t.setName("xixi")
print("name:%s"%t.getName())
print("is alive",t.is_alive())
print("Daemon",t.isDaemon())