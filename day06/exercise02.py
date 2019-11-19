"""
自定义线程类
"""
from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target=""):
        super().__init__(target) # 此行不能动
    # super().run(*self.args,*self.kwargs)
    # def start(self):
    #     self.run()
    # def run(self):
    #     self.target(*self.args,**self.kwargs)
    #
    # def join(self):
    #     pass
    def run(self):
        pass


####################################################
# 测试函数
def player():
    print("11111")

t = MyThread(target=player)
t.start() # 以一个线程去执行player函数
t.join()





