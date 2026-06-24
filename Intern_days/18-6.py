#class:-class is blueprint of object
#constructor:-special member function,constructor is call when object is created
#default constructor:-

'''class Employee:
    def __init__(self):
        self.name="kirtika"
        self.salary=3000
    def Display(self):
        print("employee name is",self.name)
        print("salary is",self.salary)
obj=Employee()
obj.Display() 

class Student:
    def __init__(self):
        self.name="kirtika"
        self.age=18
    def Display(self):
        print("Student name is",self.name)
        print("Age is",self.age)
s=Student()
s.Display()  

#parameterized constructor:-
class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Display(self):
        print("employee name is",self.name)
        print("salary is",self.salary)
obj=Emp("Aniket",45000)
obj.Display() 
    
#Inheritance:-a child class aquires the properties of parent class
class Animal:
    def __init__(self):
        self.name=" "
    def show(self):
        print(f"animal name is {self.name}")
class Cat(Animal):
    def make_sound(self):
        return "cat sound is meow"
c=Cat()
c.name="cat"
print(c.name)
print(c.make_sound())

class Father:
    def __init__(self):
        self.fname="abc"
        def father(self):
            print(f"father name is {self.fname}")
class Mother:
    def __init__(self):
        self.mname="xyz"
        def mother(self):
            print(f"father name is {self.mname}")
class Child(Father,Mother):
    def __init_(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.name="pqr"
    def Child(self):
        print(f"child name is {self.name}") 
c=Child()
c.father()
c.mother()
c.child()   '''

class Grandfather:
    def __init__(self):
        self.fname="abc"
        def grandfather(self):
            print(f"father name is {self.fname}")
class Father(Grandfather):
    def __init__(self):
        self.mname="xyz"
        def grandmother(self):
            print(f"father name is {self.mname}")
class Child(Father):
    def __init_(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.name="pqr"
    def Child(self):
        print(f"child name is {self.name}") 

c=Child()
c.grandfather()
c.father()
c.child()

            






















