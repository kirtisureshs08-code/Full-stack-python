#default argument:-parameter with fallback values
'''def student(name,age=17):
    print(f"name is{name}")
    print(f"age is {age}")

student("kirtika") 
student("kirti",20)
student(age=17,name="kirika")   

#variable length arguments:- use *args and **kwargs when the no of arguments isnt known in advance.
#*args:-
def number(*args):
    for i in args:
        print(i)
number(1,2,3,4,5,6,7)  
number('apple','kiwi','orange',True,200)      

def information(name,*args):
    print("name is ",name)
    for i in args:
        print(i)
information("krushna",45,67,89,198)    

def Sum(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
Sum(1,2,3,4,5,6,7,8,9,10)  

#**kwargs:-
def student(name,**kwargs):
    print("name is ",name)
    for k,v in kwargs.items():
        print(f"{k}==>{v}")
student(name='kirti',sub1=67,sub2=68,sub3=90)        

#Lambda Function:-
add=lambda x,y:x+y
print(add(20,30))

compare=lambda a,b:a if a>b else b
print(compare(20,10))

num=int(input("Enter number"))
ch=lambda num:True  if num%2==0 else False 
print(ch(num)) '''

#filter() & map() Functions:-
l=[1,2,3,4,5,6,7,8]
even=lambda x: x%2==0
even_list=list(filter(even,l))
print(even_list)

#map():-
sqr=lambda a:a**2
sqr_list=list(map(sqr,l))
print(sqr_list)

#reduce:-generate single value
from functools import reduce
add=lambda a,b:a+b
total=reduce(add,l)
print(total)
