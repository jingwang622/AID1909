from socket import *
# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
# 设置端口立即被重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 设置链接本机网络地址
sockfd.bind(('127.0.0.1',8888))
# 设置监听
sockfd.listen(1024)
while True:
    print("等待链接....")
    c,addr= sockfd.accept()
    print("已经链接：...")
    data = c.recv(1024)
    print(data)