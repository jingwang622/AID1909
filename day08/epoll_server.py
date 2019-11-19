"""
poll_server.py 完成tcp并发
重点代码： 创建监听套接子先进行监控
        产生新的套接子也加入到监控中
"""
from socket import *
from select import *

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建epoll对象
ep = epoll()
ep.register(s,EPOLLIN) # 将s设置关注

# 创建一个查找字典，用于他哦难过文件描述副寻找其对应的io对象
fdmap = {s.fileno():s}
# 循环监控
while True:
    events = ep.poll()  # 阻塞等待io发生
    print("你有新的io需要出发哦")
    print(events)
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            ep.register(c,EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            #
            data = fdmap[fd].recv(1024).decode()
            print(data)
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            fdmap[fd].send(b"ok")
