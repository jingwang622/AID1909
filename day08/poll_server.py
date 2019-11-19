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

# 创建poll对象
p = poll()
p.register(s,POLLIN) # 将s设置关注

# 创建一个查找字典，用于他哦难过文件描述副寻找其对应的io对象
fdmap = {s.fileno():s}
# 循环监控
while True:
    events = p.poll()  # 阻塞等待io发生
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            p.register(c,POLLIN | POLLERR)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            #
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
