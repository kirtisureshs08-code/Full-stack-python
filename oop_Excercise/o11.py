class Rectangle:
    def area(self):
        self.len=10
        self.wid=2.3
        print("area of rectangle:",self.len*self.wid)
class Circle(Rectangle):
    def area(self):
        self.r=5
        print("radius of circle:",self.r*self.r)
class Triangle(Circle):
    def area(self):
        self.base=6
        self.hei=8
        print("triangle area:",0.5*self.base*self.hei)
s=Triangle()
s.area()  
s1=Circle()                      
s1.area()
s2=Rectangle()
s2.area()