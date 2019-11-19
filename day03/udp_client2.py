"""
udp_client.py udp客户端流程
"""
from socket import *

# 服务端地址
ADDR = ('172.40.74.158',8888)
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())
