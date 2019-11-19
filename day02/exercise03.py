"""
练习1：编写额一个程序，向一个文件（log.txt)中不断写入内容，要求每2秒写入一行，每行内容：
1. 2019-11-11 18：19：10
2. 2019-11-11 18：19：12
如果程序结束，再次启动时，要求序号可以衔接
"""
import time

num = 0
# f = open("log.txt","a+")
# # for line
# while True:
#     time.sleep(2)
#     num += 1
#     time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#     data = "%d. %s\n"%(num,time_str)
#     f.write(data)
#     f.flush()
f = open("log.txt","a+")
print(f.read(1024))
f.write("222222222222222")
# f.seek(0)
print(f.read(1024))






