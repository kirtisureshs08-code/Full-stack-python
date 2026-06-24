#hiearchical
class Father:
    def __init__(self):
        self.fname="xyz"
    def father(self):
            print(f"father name is {self.fname}")
class Child1(Father):
    def __init__(self):
        Father.__init__(self)
        self.cname="pqr"
    def child(self):
            print(f"1st child name is {self.cname}")
class Child2(Father):
    def __init__(self):
        Father.__init__(self)
        self.c1name="str"
    def child1(self):
            print(f"1st child name is {self.c1name}") 
c=Child1()
c.father()
c.child()

c1=Child2()
c1.father()
c1.child1()


#Hybrid
class School:
    def school(self):
        print("this ih school class method") 

class Student1(School):
    def show1(self):
        print("this is student 1st method")       

class Student2(School):
    def show2(self):
        print("this is student 2nd method")  

class Student3(Student1,School):
    def show3(self):
        Student2.show2(self)
        print("3rd method")

s=Student3()
s.school()
s.show1()
s.show3()

#polymorphism:same function name behaves different based on input.
#polymorphism with inheritance:-a child class caan redefine parent method to change its behavior
class Vehical:
     def Display(self):
          print("vehical class")
class Bus(Vehical):
     def Display(self):
          super().Display()
          print("this is road transport mode vehical")
b=Bus()
b.Display()

#Encapsulation:-
class Parent:
     def __init__(self):
          self.__a=10     #private access specifier
          self._b=15      #protected access specifier
     def Details(self):
          print("value of parent class is",self.__a)
          print("value of parent class is",self._b)
class Child(Parent):
     def __init__(self):
          super().__init__()
     def show(self):
          print("value of child class is",self._b)
obj=Child() 
obj.Details()
obj.show()
print(obj._b)


#abstraction:-
from abc import ABC,abstractmethod
class Vehical(ABC):
     def __init__(self):
          self.model_name="Creta"
          self.year=2000
     @abstractmethod
     def Details(self):
          pass
class Car(Vehical):
     def __init__(self):
          super().__init__()
     def Details(self):
          print(self.model_name)
          print(self.year)
c=Car()
c.Details()                         