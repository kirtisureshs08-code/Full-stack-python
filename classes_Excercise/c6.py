class Circle:
    def __init__(self):
        self.radius=5.4
    def cal_area(self):
        area=3.14*self.radius*self.radius
        print(area)
b=Circle()
b.cal_area()