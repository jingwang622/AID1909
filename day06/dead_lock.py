"""
模拟死锁产生条件
"""
from time import sleep
from threading import Thread,Lock

# 账户类
class Account:
    def __init__(self, id, balance, lock):
        self.id = id   # 用户
        self.balance = balance # 存款
        self.lock = lock # 锁

    # 存钱
    def deposit(self,amount):
        self.balance += amount

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount

    # 查看余额
    def get_balance(self):
        return self.balance



# 模拟转账过程
def transfer(from_,to,amount):
    from_.lock.acquire()
    from_.withdraw(amount)
    from_.lock.release()
    sleep(0.1)

    to.lock.acquire()
    to.deposit(amount)
    to.lock.release()




# 产生两个账户
Tom = Account('Tom',5000,Lock())
Abby = Account("Abby",8000,Lock())

t1 = Thread(target=transfer,args=(Tom,Abby,2000))
t2 = Thread(target=transfer,args=(Abby,Tom,3000))
# transfer(Tom,Abby,2000)
# print("Tom:",Tom.get_balance())
# print("Abby:",Abby.get_balance())
t1.start()
t2.start()
t1.join()
t2.join()


print("Tom:",Tom.get_balance())
print("Abby:",Abby.get_balance())