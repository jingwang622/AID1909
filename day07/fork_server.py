"""
fork_server.py  fork多进程网络并发
"""
import os
from socket import *
import signal

ADDR = ("0.0.0.0",8888)
# 创建套接子
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 链接
s.bind(ADDR)
# 设置监听
s.listen(3)

# 处理僵尸进程
signal.signal((signal.SIGCHLD,signal.SIG_IGN))

print("LIsten the port 8888...")
# 与客户端交互，处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(b"ok")
    c.close()

# 循环等待客户端链接
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        s.close()
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        # 处理客户端具体请求
        s.close()
        handle(c)
        os._exit(0) # 处理完客户端请求后子进程退出
    c.close()

