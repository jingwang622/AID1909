from socket import *
socketfd = socket(AF_INET,SOCK_DGRAM)

ADDR = ('172.40.74.170',8881)

while True:
    data = input("请输入单词：")
    if not data:
        break
    socketfd.sendto(data.encode(),ADDR)
    msg,addr = socketfd.recvfrom(1024)
    print(msg.decode())


socketfd.close()