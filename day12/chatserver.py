from socket import *
# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
# 设置端口立即被重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 设置链接本机网络地址
sockfd.bind(('127.0.0.1',8888))
# 设置监听
sockfd.listen(1024)
name_dict = {}

def login(name,addr):
    for item in name_dict:
        if name == item:
            data = "登录失败"
            break
    else:
        name_dict[name] = addr
        data = "登录成功"
    return data


while True:
    print("等待链接....")
    try:
        c,addr= sockfd.accept()
        print("已经链接：...")
    except:
        c.close()
        sockfd.close()
    while True:
        data = c.recv(1024)
        message_list = data.decode().split(" ")
        if message_list[0] == "L":
            # 登录
            result = login(message_list[1],addr)
            print(result)
            c.send(result.encode())

c.close()
sockfd.close()