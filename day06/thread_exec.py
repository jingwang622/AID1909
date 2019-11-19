"""
开启多个线程,分别从多个目标位置拷贝文件的不同部分,
然后在当前目录下合成一个完整的文件.
"""
from threading import Thread,Lock
import os
# 资源库
urls = [
        "/home/tarena/桌面/",
        "/home/tarena/公共的/",
        "/home/tarena/音乐/",
        "/home/tarena/视频/",
        "/home/tarena/模板/",
        "/home/tarena/下载/",
    ]
filename = input("要下载的文件:")
timg_list = []
file_path = "/home/tarena/timg.jpg"
fw = open(file_path, "wb")


def own_file_list(filename):
    for url in urls:
        if os.path.exists(url+filename):
            timg_list.append(url+filename)

def load(target_file_path,block_size,offset):
    fr = open(target_file_path,"rb")
    fr.seek(offset)
    data = fr.read(block_size)
    print(data)
    with Lock():
        fw.seek(offset)
        fw.write(data)

def main():
    own_file_list(filename)
    print("------------------")
    print(timg_list)
    timg_num = len(timg_list)
    if timg_num == 0:
        print("没有资源")
        os._exit(0)
    sumsize = os.path.getsize(timg_list[1])
    print("=====================")
    print(sumsize)
    block_size = sumsize // len(timg_list) + 1
    print(block_size)
    t_list = []
    offset = 0
    for file in timg_list:
        t = Thread(target=load,args=(file,block_size,offset))
        offset += block_size
        t.start()
        t_list.append(t)
    [t.join() for t in t_list]




main()
