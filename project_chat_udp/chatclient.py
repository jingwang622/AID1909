from socket import *
# 服务器地址
server_addr = ('127.0.0.1', 8888)

def login(sockfd):
    while True:
        name = input("请输入姓名：")
        message = "L %s" % name
        sockfd.sendto(message.encode(),server_addr)
        msg,addr = sockfd.recvfrom(1024)
        if not msg:
            break
        if msg.decode() == "OK":
            return "登录成功"
        else:
            print(msg.decode())
            continue


def chat(sockfd):
    print("111111111")
    while True:
        pass


def do_request(sockfd):
    if login(sockfd) == "登录成功":
        chat(sockfd)




def main():
    # 创建套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    # 发送消息
    do_request(sockfd)


if __name__ == '__main__':
    main()