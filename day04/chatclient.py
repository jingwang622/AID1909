"""
发送请求，获取结果
"""
import sys
from socket import *
import os
# 服务器地址
ADDR = ('127.0.0.1',8888)


def send_msg(s, name):
    while True:
        try:
            message = input("请输入聊天内容：")
        except KeyboardInterrupt:
            message == "##"
        if message == "##":
            msg = "E %s %s"%(name,message)
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" %(name,message)
        s.sendto(msg.encode(),ADDR)


def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(1024 * 1024)
        except KeyboardInterrupt:
            data = b"EXIT"
        # 收到EXIT时退出接收进程
        if data.decode() == "EXIT":
            break
        print(data.decode())


def chat(s, name):
    pid = os.fork()
    if pid < 0:
        os._exit(0)
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

# 启动函数，构建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR) # 发送请求
        data,addr = s.recvfrom(128) # 接收反馈
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # 进行聊天
    chat(s,name)



if __name__ == '__main__':
    main()