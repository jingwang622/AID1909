


class BankController:
    def __init__(self):
        self.person_list = []
    # 重复确认密码
    def repeat_confirm(self,repasswd):
        pass
    # 开户(open)
    def open(self,person,repasswd):
        # 确认密码输入三次以内，则返回True，三次都确认失败，返回False
        num = 3
        while num:
            num -= 1
            if person.card.password == repasswd:
                return True
            pass
    # 存款(deposit)
    def deposit(self):
        pass
    # 查询(search)
    def search(self):
        pass
    # 取款(withdraw)
    def withdraw(self):
        pass
    # 转账(transfer)
    def transfer(self):
        pass
    # 销户(cancel)
    def cancel(self):
        pass
    # 锁定(locking)
    def lock(self):
        pass
    # 解锁(unlock)
    def unlock(self):
        pass
    # 补卡(card)
    def addcard(self):
        pass
    # 改密(passwd)
    def passwd(self):
        pass
    # 退出(quit)
    def quit(self):
        pass

