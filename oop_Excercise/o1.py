class Person:
    def display(self):
        print("parent class")
class Student(Person):
    def display1(self):
        print("child class")        
s=Student()
s.display()
s.display1()