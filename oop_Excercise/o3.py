class Employee:
    def display(self):
        print("parent class")
class Manager(Employee):
    def display1(self):
        print("child class")        
s=Manager()
s.display()
s.display1()