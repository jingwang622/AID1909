# 功能 : 类似qq群功能
# 【1】 有人进入聊天室需要输入姓名,姓名不能重复
# 【2】 有人进入聊天室时,其他人会收到通知:xxx 进入了聊天室
# 【3】 一个人发消息,其他人会收到:xxx : xxxxxxxxxxx
# 【4】 有人退出聊天室,则其他人也会收到通知:xxx退出了聊天室
# 【5】 扩展功能:服务器可以向所有用户发送公告:管理员消息: xxxxxxxxx
from socket import *
import os,sys
 # 创建udp套接字
ADDR = ("0.0.0.0",8888)
user = {}
# 进入聊天室
def do_login(s,name,addr):
    if name in user:
        s.sendto("您的名字太受欢迎了".encode())
        return
    s.sendto(b'OK',addr) # 允许进入
    # 通知其他人
    msg = "\n欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr # 加入字典

# 进行聊天
def do_chat(s, name,message):
    msg = "\n%s:%s"%(name,message)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
# 接收请求，任务分发


def do_exit(s, name):
    # 防止用户不再user
    if name not in user:
        return
    msg = "\n%s 退出聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"EXIT",user[name])
    del user[name]


def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        # 判断请求类型
        tmp = data.decode().split(" ",2)# 将请求拆分
        if tmp[0] == "L":
            do_login(s,tmp[1],addr)
        elif tmp[0] == "C":
            do_chat(s,tmp[1],tmp[2])
        elif tmp[0] == "E":
            do_exit(s, tmp[1])
        print(data)

# 网络搭建
def main():
    # udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    # 绑定地址
    s.bind(ADDR)
    # 接收客户端请求
    pid = os.fork()
    if pid == 0:
        while True:
            msg = "C 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)



if __name__ == '__main__':
    main()

