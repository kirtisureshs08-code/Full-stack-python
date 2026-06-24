class Product:
    def __init__(self,id,name,quantity,price):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
    def add_stock(self,qty):
        self.quantity+=qty    
    def remove_stock(self,qty):
        if qty<=self.quantity:
            self.quantity-=qty
        else:
            print("not enogh stock")
    def display_p(self):
        print("produvt id:",self.id)
        print("product name:",self.name)
        print("quantity:",self.quantity)   
        print("price:",self.price)
p=Product(1,"laptop",10,50000)
p.add_stock(5)
p.remove_stock(3)
p.display_p()

