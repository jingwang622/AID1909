"""
ftp服务器  服务端
env：python3.6
多线程并发，socket，文件IO
"""
import os,sys
from socket import *
import signal
from threading import Thread

# 全局变量
from time import sleep

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/ftp" # 文件库位置

# 文件处理功能
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()
    # 空置函数，任务分发
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            datalist = data.decode().split(" ")
            if data.decode() == "list":
                self.do_list()
            elif datalist[0] == "get":
                self.do_get_file(datalist)
            elif datalist[0] == "put":
                self.do_put_file(datalist)
            else:
                self.exit()
    # 文件列表发送
    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
        # 发送文件列表
        filelist = "\n".join(files)
        sleep(0.1)
        self.connfd.send(filelist.encode())
    def do_get_file(self):
        pass

    def do_put_file(self,datalist):
        files = os.listdir(FTP)
        filepath = datalist[1].split("/")
        if filepath[-1] in files:
            self.connfd.send("文件已存在".encode())
        else:
            self.connfd.send(b"OK")
            fw = open(FTP+"/"+filepath[-1], "wb")
            while True:
                data = self.connfd.recv(1024)
                print(data)
                if data == b"##":
                    break
                fw.write(data)
            fw.close()

    def exit(self):
        pass


# 网络搭建（多线程并发）
def main():
    # 创建套接子
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 链接
    s.bind(ADDR)
    # 设置监听
    s.listen(3)

    print("LIsten the port 8888...")
    # 循环等待客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        # 创建线程处理客户端请求
        ftp = FTPServer(c)
        ftp.start()

if __name__ == '__main__':
    main()


