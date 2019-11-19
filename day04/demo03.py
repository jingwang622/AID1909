"""
获取进程号
"""
from time import sleep
import os
import sys
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("child PID:",os.getpid())
    sys.exit(2)
else:
    while True:
        pass
