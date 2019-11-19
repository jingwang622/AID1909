from socket import *
import time
# 创建tcp套接字
sockfd = socket() # 默认参数是tcp

# 连接服务端
server_addr = ("127.0.0.1",8888)
sockfd.connect(server_addr)

# 发消息
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    # if data == "##":
    #     break

    msg = sockfd.recv(1)
    print("server:",msg.decode())

# 关闭套接字
sockfd.close()