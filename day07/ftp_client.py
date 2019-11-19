"""
ftp文件服务 客户端
"""
from socket import *
import time

from day03.data_client import sockfd

ADDR = ("127.0.0.1",8080)
task_tuple = ("list",
             "get file",
             "put file",
             "exit"
             )

class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send("list".encode())# 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        print(data)
        if data == "OK":
            # 一次性接收
            data = self.sockfd.recv(1024 * 1024).decode()
            print(data)
        else:
            print(data) # 不成功原因


    def put_file(self, choice,filepath):
        message = choice.strip() + " " + filepath
        self.sockfd.send(message.encode())
        data = self.sockfd.recv(128).decode()
        print(data)
        if data == "OK":
            print("=============")
            fr = open(filepath,"rb")
            print(filepath)
            while True:
                data = fr.read(1024)
                print(data)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fr.close()
        else:
            print(data)

# 网络搭建(和服务端建立通信，然后通过打印命令提示选择执行的功能)


def main():
    # 创建tcp套接字
    sockfd = socket() # 默认参数是tcp
    # 连接服务端
    server_addr = ("127.0.0.1",8888)
    sockfd.connect(server_addr)
    ftp = FTPClient(sockfd)
    # 发消息
    while True:
        print('''
            ##################
                 list
                 get  file
                 put  file
                 exit 
            ##################
        ''')
        choice = input("请输入选择：")
        if choice.strip() == "list":
            ftp.do_list()
        elif choice.strip() == "get":
            sockfd.send(choice.encode())
        elif choice.strip() == "put":
            filepath = input("输入文件名")
            # filepath = "/home/tarena/图片/timg.jpg"
            # message = choice.strip() + " " + filepath
            ftp.put_file(choice,filepath)

        elif choice.strip() == "exit":
            sockfd.send(choice.encode())
        else:
            print("请循环输入")

        # msg = sockfd.recv(128)
        # print("server:",msg.decode())

    # 关闭套接字
if __name__ == '__main__':
    main()