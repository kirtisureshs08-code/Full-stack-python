class Vehicle:
    def display(self):
        print("parent class")
class Car(Vehicle):
    def display1(self):
        print("child class")        
s=Car()
s.display()
s.display1()