#Q.1
'''A=int(input("Enter Any numbers:"))
B=int(input("Enter Any numbers:"))
print("Adiition of 2 num:",A+B)

#Q.2
len=10
h=20
w=5.6
print("Area of Rectangle:",len*h*w)

#Q.3
num=int(input("Enter Any numbers:"))
print("Square of num:",num**2)
print("Cube of num:",num**3)

#Q.4
Q=int(input("Enter Any numbers:"))
R=int(input("Enter Any numbers:"))
print("Quotient:",Q//R)
print("Reminder:",Q%R)

#Q.5
min=int(input("Enter Minutes:"))
print("Hours:",min//60)
print("Remaining minutes:",min%60)


#Q.6
s=30
d=40
if s==d:
    print("s is equal to d")
else:
    print("both num are not same")    

#Q.7
num1=50
num2=40
if num1>num2:
    print("num1 is larger")
else:
    print("num2 is larger")

#Q.8
a=10
b=20
c=30
if a>b and a>c :
    print("A is largest")
elif b>a and b>c:
    print("B is largest")
else:
    print("C is largest")

#Q.9
marks=int(input("Enter Marks"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Q.10
age=int(input("Enetr Age"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")    
print("Age is ",age)
 
#Q.11
p=2
q=3
p+=q
print(p)
p-=q
print(p)
p*=q
print(p)
p/=q
print(p)

#Q.12
balance=10000
deposit=int(input("Enter deposit amount:"))
balance+=deposit
withdraw=int(input("Enter withdraw amount:"))
balance-=withdraw
print("Final balance:",balance)

#Q.13
C=5
backlog=8
if C>7 and backlog<3:
    print("eligible for placement")
else:
    print("not eligible for placement")    

 #Q.14
age=int(input("Enetr Age"))
if age>=18:
    print("eligible for club entry")
else:
    print("not eligible for club entry")    

#Q.15
blocked="kirtika"
unblocked="neha"
if "kirtika" not in blocked :
    print("user is unblocked")
else:
    print("user is blocked")    

#Q.16
str="neha"
char='h'
if char in str :
    print("character is found")
else:
    print("character is not found")

#Q.17
list=["kirtika","neha"]
if "kirtika" in list:
    print("yes")
else:
    print("no")    

#Q.18
t=(1,2,3)
if 4 in t:
    print("num in t")
else:
    print("num not in t")


#Q.19
w=[1,2,3,4,5,6,7]
z=w
if w is z:
    print("same object")
else:
    print("diff object")    


#Q.20
l1=[2,3,4]
l2=[1,2,5] 
if l1==l2:
    print("both are equal")          
else:
    print("both are not equal")    '''

#Q.21
a1=5
a2=10
op=input("Enter op:")
if op== '+':
    print(a1+a2)
elif op=='-':
    print(a1-a2)
else:
    print(a1*a2)    