"""
使用tcp完成从客户段向服务端发送一个文件，
文件类型可能是二进制文件也可能是文本文件
文件定义
温馨提示：
发送端：read() --> send()
接收:recv() --> write()
"""
import socket

sockfd = socket.socket()
sockfd.bind(("127.0.0.1",8888))
sockfd.listen(1024)

print("等待链接.....")
connfd,addr = sockfd.accept()
print("链接了：",addr)
fr = open("timg1.jpg", "ab")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    fr.write(data)
        # if data == b"##":
        #     break
fr.close()
connfd.close()
sockfd.close()



