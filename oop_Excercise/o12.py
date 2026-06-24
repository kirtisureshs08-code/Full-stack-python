class Dog:
    def sound(self):
        print("dogs Bark")
class Cat(Dog):
    def sound(self):
        print("meow")        
class Cow(Cat):
    def sound(self):
        print("moo")        
c=Cow()
c.sound()
c1=Cat()
c1.sound()
c2=Dog()
c2.sound()        