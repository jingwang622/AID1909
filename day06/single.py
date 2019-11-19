import time
from GIL_test import *
time_start = time.time()
for i in range(10):
    count(1,1)

time_end = time.time()
print(time_end-time_start)