"""
webframe 配置文件
功能：
httpserver部分需要与两端建立通信
webFrame部分采用多路复用接收并发请求
数据传递使用json格式
"""
from socket import *
import json
from settings import *
from threading import Thread
from urls import *
from views import *

# 将应用的功能封装在类中
class Application:
    def __init__(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind((frame_ip,frame_port))
    def start(self):
        self.sock.listen(3)
        print("Running web server on %s"%frame_port)
        while True:
            connfd,addr = self.sock.accept()
            t = Thread(target=self.handle,args=(connfd,))
            t.setDaemon(True)
            t.start()
    def handle(self,connfd):
        # 接受请求
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request:{"method": "GET", "info": "/"}
        if request['method'] == "GET":
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])

            else:
                response = self.get_data(request['info'])
            response = json.dumps(response)
            connfd.send(response.encode())
            connfd.close()
        elif request['method'] == "POST":
            pass

    def get_html(self,info):
        if info == "/":
            filename = STATIC_DIR + '/index.html'
        else:
            filename = STATIC_DIR + info
        try:
            f = open(filename, 'r')
        except:
            return {'status':'404','data':open(STATIC_DIR+'/404.html').read()}
        else:
            return {'status':'200','data':f.read()}
    # 数据处理函数
    def get_data(self, info):
        for url,func in urls:
            if info == url:
                return {'status':'200','data':func()}
        return {'status':'404','data':'sorry'}


if __name__ == '__main__':
    app = Application()
    app.start() # 启动服务

