class Student:
    def __init__(self):
        self.__name="kirtika"
        self.__marks=82
    def Display(self):
        print("Student name is ",self.__name)
        print(f"Student marks is {self.__marks}")    
s=Student()
s.Display()        