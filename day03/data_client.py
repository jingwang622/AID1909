from socket import *
import time
import struct
# 创建tcp套接字
sockfd = socket(AF_INET,SOCK_DGRAM) # 默认参数是tcp

# 连接服务端
server_addr = ("127.0.0.1",8888)
# 发消息
st = struct.Struct("i16sii")
student_list = [(1,'Lily',10,78),
        (2,'Tom',9,91),
        (3,'Jame',8,91),
        (4,'Abby',11,87),
        (5,'Leli',34,90),
        ]
for id,name,age,score in student_list:
    student_data = st.pack(id,name.encode(),age,score)
    sockfd.sendto(student_data,server_addr)

    # if data == "##":
    #     break

# 关闭套接字
sockfd.close()