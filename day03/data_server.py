import socket
import struct
sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sockfd.bind(("127.0.0.1",8888))

st = struct.Struct("i16sii")
f = open("student.txt",'a')
while True:
    student_data,addr = sockfd.recvfrom(1024)
    data = st.unpack(student_data)
    # 写入内容
    info = "%d %s %d %d\n" % (data[0],data[1].decode().strip("\x00"),data[2],data[3])
    f.write(info)

sockfd.close()
f.close()



