import os
pid = os.fork()
if pid < 0:
    print("Create process faild")
elif pid == 0:
    print("THe new process")
else:
    print("THe old process")
print("FOrk test over")