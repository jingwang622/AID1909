class Card:
    def __init__(self, password="", cardno="", money=0.0, islock=False):
        self.password = password
        self.cardno = cardno
        self.money = money
        self.islock = islock
