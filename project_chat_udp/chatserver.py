from socket import *
import sys,os
name_dict = {}

def login(sockfd,name,addr):
    if name in name_dict:
        sockfd.sendto("名字有重复".encode(),addr)
    else:
        name_dict[name] = addr
        info = "%s 进入群聊" % name
        print(info)
        for i in name_dict:
            if i == name:
                sockfd.sendto(b"OK", addr)
            else:
                sockfd.sendto(info.encode(),name_dict[i])



def sendmessade(content):
    pass

def exit():
    pass

def handle(sockfd):
    while True:
        message,addr = sockfd.recvfrom(1024)
        message_list = message.decode().split(" ")
        if message_list[0] == "L":
            login(sockfd,message_list[1],addr)
        elif message_list[0] == "S":
            sendmessade(sockfd,message_list[1],addr)
        elif message_list[0] == "E":
            exit()

def main():
    # 创建套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    # 设置端口立即被重用
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 设置链接本机网络地址
    sockfd.bind(('0.0.0.0', 8888))
    handle(sockfd)
    sockfd.close()


if __name__ == '__main__':
    main()
