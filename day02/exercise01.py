"""
作业 ：  编写程序完成
        用input输入一个文件名称（可以包含路径）
        将这个文件拷贝到主目录下
        注意： 文件可能文本文件也可能是二进制文件
        要求： 文件不允许一次性读取
"""
import os
str = input("请输入文件路径:")
file1name = str.split('/')[-1]
try:
    file1 = open(file1name,"rb")
except Exception as e:
    print(e)
else:
    file2 = open("/home/tarena/" + file1name,'wb')
    # for line in file1:
    #     file2.write(line)
    while True:
        data = file1.read(1024)
        if not data:
            break
        file2.write(data)
file1.close()
file2.close()




