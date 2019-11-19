import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sockfd.bind(("127.0.0.1",8888))
sockfd.listen(1024)
while True:
    print("等待链接.....")
    connfd,addr = sockfd.accept()
    print("链接了：",addr)
    while True:
        data = connfd.recv(1024)
        # if data == b"##":
        #     break
        if not data:
            break
        print("收到:",data.decode())
        n = connfd.send("收到-".encode())
        print("发送了：%d bytes" % n)
    connfd.close()
sockfd.close()



