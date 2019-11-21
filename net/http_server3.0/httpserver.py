"""
http server 部分的主体程序
功能：
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
from socket import *
from config import *
from select import *
import re
import json
# 用户和webframe交互
def connect_frame(env):
    """

    :param env: 要发送的字典
    :return: 从webframe得到的数据
    """
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except:
        print("连接不到webframe")
        return
    # 发送字典{‘method’:xxx,'info':...}
    data = json.dumps(env)
    s.send(data.encode())
    # 接收返回的数据
    data = s.recv(1024*1024*10).decode()
    print(data)
    if data:
        return json.loads(data)
# 封装http类
class HttpServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST,PORT)
        self.create_socket()

    def create_socket(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind(self.address)
    # 启动函数
    def serve_forver(self):
        self.create_socket()
        self.sock.listen(3)
        print("你启动了http服务,监听%s端口."%self.port)
        # 创建epoll对象
        self.ep = epoll()
        self.ep.register(self.sock,EPOLLIN) # 将sock添加关注
        self.fdmap = {self.sock.fileno():self.sock}
        # 循环监控io
        while True:
            events = self.ep.poll()# 阻塞等待的io发生
            print("你有新的io要处理哦")
            for fd,event in events:
                if fd == self.sock.fileno():
                    connfd,addr = self.sock.accept()
                    print("已连接一个服务端")
                    self.ep.register(connfd,EPOLLIN|EPOLLET)
                    self.fdmap[connfd.fileno()] = connfd
                else:
                    # 浏览器发送了http请求
                    self.handle(self.fdmap[fd])
                    # data = self.fdmap[fd].recv(4096)
                    # print(data)

    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096).decode()
        # 向webframe 发送请求类型和请求内容
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern,request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)
            self.response(connfd,data)
    def response(self,connfd,data):
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK \r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
            response = responseHeaders + responseBody
            connfd.send(response.encode())
        elif data['status'] == "404":
            responseHeaders = "HTTP/1.1 404 NOT FOUND \r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
            response = responseHeaders + responseBody
            connfd.send(response.encode())


if __name__ == '__main__':
    httpd = HttpServer()
    httpd.serve_forver() # 启动服务