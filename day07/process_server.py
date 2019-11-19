"""
thread_server.py
重点代码
"""
import signal
from multiprocessing import Process
from socket import *
from threading import Thread
import sys
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
# 与客户端交互，处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(b"ok")
    c.close()
print("LIsten the port 8888...")
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        s.close()
        sys.exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建线程处理客户端请求
    p = Process(target=handle,args = (c,))
    p.daemon = True
    p.start() # 主线程服务结束，分支线程也退出服务


