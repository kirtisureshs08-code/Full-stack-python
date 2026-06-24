class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def car(self):
        print(self.brand)
        print(self.model)
        print(self.price)
c=Car("MarutiSuzuki","inovo",2900000)   
c.car()         