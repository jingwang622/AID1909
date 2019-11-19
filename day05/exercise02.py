import os,sys
from time import *
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(2)
    print("Child PID:",os.getpid())
    sys.exit()
else:
    sleep(300)
    print("parent PID:", os.getpid())
