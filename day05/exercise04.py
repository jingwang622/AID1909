"""
求1--100000以内质数之和，并统计整个过程所用的时间
温馨提示： 将求和过程封装为函数
        通过装饰器获取函数执行时间即可
质数：只能被1和它本身整除的整数，1不是质数
"""
from time import time
from multiprocessing import Process
# 求运行时间装饰器
def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = f(*args,**kwargs)
        end_time = time()
        print("%s函数执行时间:%.8f"%(f.__name__,end_time-start_time))
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n:int)->bool:
    if n <= 1:
        return False
    for i in range(2,int(n)):
        if n % i == 0:
            return False
    return True

def prime1():
    pr = []
    for i in range(1,25000):
        if isPrime(i):
            pr.append(i)
    print("Sum:",sum(pr))
def prime2():
    pr = []
    for i in range(25001,50000):
        if isPrime(i):
            pr.append(i)
    print("Sum:",sum(pr))
def prime3():
    pr = []
    for i in range(50001,75000):
        if isPrime(i):
            pr.append(i)
    print("Sum:",sum(pr))

def prime4():
    pr = []
    for i in range(75001,100001):
        if isPrime(i):
            pr.append(i)
    print("Sum:",sum(pr))

@timeit
def haha():
    p1 = Process(target=prime1)
    p1.start()

    p2 = Process(target=prime2)
    p2.start()

    p3 = Process(target=prime3)
    p3.start()


    p4 = Process(target=prime4)
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

haha()









