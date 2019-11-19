"""
http_server.py
功能：1.获取来自浏览器的请求（request）
     2.如果请求内容为“/”那么将Index.html给浏览器
     3.如果不是“/”返回给客户端404
"""
from socket import *
ADDR = ('127.0.0.1', 8000)
def request(con):
    str_base = con.recv(1024 * 4)
    str = str_base.decode()
    path = str.split(" ")[1]
    data = ""
    if path == "/":
        f = open("index.html", "r")
        for line in f:
            data += line
        f.close()
        whole_data = """HTTP/1.1 200 OK
Content-Type:text/html;charset="UTF-8"


        """ + data
    else:
        whole_data = """HTTP/1.1 404 notfound
Content-Type:text/html;charset="UTF-8"


        """ + "sorry"
    con.send(whole_data.encode())

    con.close()


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