class Mobile:
    def __init__(self):
        self.brand="samsung"
        self.model="1234"
        self.RAM="8GB"
        self.price=40000
    def display_specs(self):
        print(self.brand)
        print(self.model)
        print(self.RAM)
        print(self.price)
m=Mobile()
m.display_specs()            