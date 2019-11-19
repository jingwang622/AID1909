"""
block_io.py
socket 套接字非阻塞实例
"""
from socket import *
from time import ctime,sleep
ADDR = ("0.0.0.0",8888)
# 创建套接子
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 链接
s.bind(ADDR)
# 设置监听
s.listen(3)


# 设置非阻塞
# s.setblocking(False)
s.settimeout(2)


f = open("log.txt","a")  # 打开一个日志文件
# 循环等待客户端链接
while True:
    print("LIsten the port 8888...")
    try:
        c,addr = s.accept()
    except Exception as e:
        sleep(3)
        f.write("%s--%s\n"%(ctime(), e))
    else:
        print("Connect from",addr)
        data = c.recv(1024)
        print(data)


s.close()