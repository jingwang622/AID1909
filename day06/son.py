from day06.father import Father


class Son(Father):
    def __init__(self,name):
        super().__init__(name)




son = Son("name")
print(son.name)
son.earn()