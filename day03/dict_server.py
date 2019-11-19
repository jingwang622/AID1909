from socket import *
# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(("0.0.0.0",8881))

# 默认r方式打开


def search_danci(word):
    f = open('dict.txt')
    for line in f:
        # 提取一行中的单词
        tmp = line.split(' ')[0]
        # 遍历的单词已经比目标大了
        if tmp > word:
            f.close()
            return "没有找到该单词"
        elif tmp == word:
            f.close()
            return line

    else:
        f.close()
        return "没有找到该单词"



while True:
# 每次取一行
    msg,addr = sockfd.recvfrom(64)
    if not msg:
        break
    # 查找单词
    search_info = search_danci(msg.decode())
    sockfd.sendto(search_info.encode(),addr)
sockfd.close()