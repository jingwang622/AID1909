class Father():
    def __init__(self,name="",money = None):
        self.name = name
        self.money = money

    def earn(self):
        print("钱",self.money)