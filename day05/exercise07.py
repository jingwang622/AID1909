"""
使用进程池完成对一个目录的备份，目录中可能有若干个普通文件
要求吧每个文件的拷贝工作作为一个进程
"""
from multiprocessing import Pool,Queue
import os
q = Queue(10)
# 进程池事件函数
def copy_file(filename,base_path,new_path):
    fr = open(os.path.join(base_path,filename),"rb")
    fw = open(os.path.join(new_path,filename),"wb")
    while True:
        data = fr.read(1024 * 10)
        if not data:
            break
        n = fw.write(data)
        q.put(n)
        # q.put(os.path.getsize(filename))
    fr.close()
    fw.close()


def main():
    sumsize = 0
    if not os.path.exists("新源文件"):
        os.mkdir("新源文件")
    base_path = os.path.join(os.getcwd(), "源文件")
    new_path = os.path.join(os.getcwd(), "新源文件")
    file_name_list = os.listdir("源文件")
    # 获取文件目录总大小
    for file in file_name_list:
        sumsize += os.path.getsize(os.path.join(base_path,file))
    print(sumsize)
    # 创建进程池
    pool = Pool(5)
    # 向进程吃队列中添加事件
    size = 0
    for file_name in file_name_list:
        pool.apply_async(func=copy_file,args = (file_name,base_path,new_path))
    # 关闭进程池
    pool.close()
    copy_size = 0
    while True:
        copy_size += q.get()
        print("拷贝了%.1f%%"%(copy_size/sumsize*100))
        if copy_size >= sumsize:
            break
    print("总共拷贝了%.1fM"%(sumsize/1024/1024))
    # 回收进程池
    pool.join()

if __name__ == '__main__':
    main()

