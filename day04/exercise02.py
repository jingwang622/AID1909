# 使用Process方法，创建两个子进程去同时复制一个文件的上
# 半部分和下半部分，并分别写入到一个新的文件中。
# 获取文件大小： os.path.getsize()
import os
from multiprocessing import Process
def read_front_file(file_path):
    """
    获取源文件大小
    :param file_path:
    :return:
    """
    sum_size = os.path.getsize(file_path)
    f = open(file_path,'r')
    data_front = ""
    data_behind = ""
    for line in f.read(os.path.getsize(file_path)//2):
        data_front += line
    num = f.tell()
    f.seek(num)

    for line in f:
        data_behind += line
    f.close()
    return (data_front,data_behind)

# def read_behind_file(file_path):
#     """
#     获取源文件大小
#     :param file_path:
#     :return:
#     """
#     sum_size = os.path.getsize(file_path)
#     f = open(file_path,'r')
#     f.seek(os.path.getsize(file_path) // 2)
#     data = ""
#     for line in f:
#         data += line
#     return data

def write_file(data,file_path):
    f = open(file_path,'a')
    f.write(data)
    f.close()

if __name__ == '__main__':
    # 原始路径
    p_list = []
    file_path = "dict.txt"
    file_path_new = "dict_new1.txt"
    data_tuple = read_front_file(file_path)
    for data in data_tuple:
        p = Process(target=write_file,args=(data,file_path_new))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()





