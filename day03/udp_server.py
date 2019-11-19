from socket import *
# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(("0.0.0.0",8888))

# 收发消息
while True:
    data,addr = sockfd.recvfrom(5)
    print("收到",data.decode())
    sockfd.sendto(b"123",addr)

sockfd.close()