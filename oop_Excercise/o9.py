class Mobile:
    def __init__(self):
        self.__price=0
    def setter(self,price):
        self.__price=price
    def getter(self):
        return self.__price       
m=Mobile()
m.setter(4000)
print("price:",m.getter())    