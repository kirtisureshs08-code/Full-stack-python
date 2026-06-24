class Rectangle:
    def __init__(self):
        self.length=10
        self.width=5.4
    def cal_area(self):
        self.result=self.length*self.width
        print(self.length)
        print(self.width)
        print(self.result)
b=Rectangle()
b.cal_area()