from socket import *
# 创建套接字
sockfd = socket()
# 服务器地址
server_addr = ('127.0.0.1',8888)
# 连接服务器
sockfd.connect(server_addr)
# 发送消息
while True:
    name = input("输入姓名：")
    message = "L " + name
    sockfd.send(message.encode())
    result = sockfd.recv(1024)
    if not result:
        break
    print(result.decode())

sockfd.close()