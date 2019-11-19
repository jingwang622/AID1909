"""
event 线程互斥方法
× 解决对共享资源的无序使用
"""
from threading import Thread,Event
# 用于线程间的通信
s = None
e = Event()
def yang():
    print("样子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()

t = Thread(target=yang)
t.start()
print("说对口令就是自己人")
print(e.is_set())
e.wait()
print(e.is_set())
if s == '天王盖地虎':
    print("宝塔真和要")
    print("确认过眼神你是对的人")
else:
    print("打死他")
t.join()
