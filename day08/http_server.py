"""
httpserver v2.0
io多路复用 和 http协议训练

接收客户端（浏览器）请求
解析客户端发送的请求
根据请求组织数据内容
将数据内容形成http响应格式返回给浏览器
"""
import os
from socket import *
from select import *

# 具体的功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        self.create_socket() # 创建套接字

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.address)

    def serve_forever(self):
        html_list = os.listdir(os.path.join(self.dir,"/"))
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        # IO多路复用循环监听客户端请求
        # 创建epoll对象
        ep = epoll()
        ep.register(self.sockfd, EPOLLIN)  # 将s设置关注

        # 创建一个查找字典，用于他哦难过文件描述副寻找其对应的io对象
        fdmap = {self.sockfd.fileno(): self.socket}
        # 循环监控
        while True:
            events = ep.poll()  # 阻塞等待io发生
            print("你有新的io需要出发哦")
            print(events)
            for fd, event in events:
                if fd == self.sockfd.fileno():
                    c, addr = fdmap[fd].accept()
                    ep.register(c, EPOLLIN | EPOLLERR)
                    fdmap[c.fileno()] = c
                elif event & EPOLLIN:
                    #
                    # data = fdmap[fd].recv(1024).decode()
                    # print(data)
                    # path = data.split(" ")[1]
                    # data = ""
                    # if path in html_list:
                    #     pass
                    self.handle(c)

    def handle(self, c):
        pass


if __name__ == '__main__':
    """
    通过HTTPServer类可以快速的搭建一个服务,帮助我展示我的网页
    使用原则 : 1. 能够为使用者实现的尽量都实现
              2. 不能替用户决定的数据量让用户传入类中
              3. 不能替用户决定的功能让用户去重写
    """
    # 用户自己设定参数
    host = '0.0.0.0'
    port = 8000
    dir = "./static"  # 网页位置

    httpd = HTTPServer(host,port,dir) # 实例化对象
    httpd.serve_forever() # 启动服务

