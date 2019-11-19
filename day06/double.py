import time
from GIL_test import *
from threading import Thread
from multiprocessing import Process
time_start = time.time()
t_list = []
for i in range(10):
    t = Process(target=count,args=(1,1))
    t_list.append(t)
    t.start()


for t in t_list:
    t.join()
time_end = time.time()
print(time_end - time_start)