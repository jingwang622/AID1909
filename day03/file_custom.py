from socket import *
import time
# 创建tcp套接字
sockfd = socket() # 默认参数是tcp

# 连接服务端
server_addr = ("127.0.0.1",8888)
sockfd.connect(server_addr)

# 发消息
data = input(">>")
f = open(data,"rb")
# for line in f:
#     sockfd.send(line)
for i in f:
    sockfd.send(i)
    # if data == "##":
    #     break

f.close()

# 关闭套接字
sockfd.close()