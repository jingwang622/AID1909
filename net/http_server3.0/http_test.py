"""
http_server.py
功能：1.获取来自浏览器的请求（request）
     2.如果请求内容为“/”那么将Index.html给浏览器
     3.如果不是“/”返回给客户端404
"""
from socket import *
import json
ADDR = ('127.0.0.1', 8080)
def request(con):
    str_base = con.recv(1024 * 4)
    d = {'status':'200','data':'ccccc'}
    msg = json.dumps(d)
    con.send(msg.encode())


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(2)

    c, addr = s.accept()
    html_name = request(c)

    s.close()

if __name__ == "__main__":
    main()