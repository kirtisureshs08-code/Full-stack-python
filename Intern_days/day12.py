#nested if statement:-place once if inside for multi-step decisions.
#eg:-
num=10
if num>5:
    if num<15:
        print("valid")

#if-elif-else ladder:-test multiple condition in order-execute the 1st that matches
a=56
b=34
print("1.addition \n2.subtraction \n3.multiplication \n4.division")
choice=int(input("Enter choice:"))
if choice==1:
    print("Addition:",a+b)
elif choice==2:
    print("subtraction:",a-b)
elif choice==3:
    print("multiplication:",a*b)
elif choice==4:
    print("division:",a/b)
else:
    print("invalid option")

#python loops:-
#for loop:-iterate over the items of any sequence(list,tuple,set,dictionary) in order.
#eg:-we want numbers traversing so use range method 
for i in range(5):
    print(i)

s="sumago"
for char in s:
    print(char)

tup=(1,2,3,4,5)
for i in tup:
    print(i)

data={'name':'sumago','address':'nsk'}
for k,v in data.items():
    #format string
    print(f"{k}==>{v}")
    
for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(2,21,2):
    print(i)    

#Nested for loop:-
rows=7
for i in range(1,rows):
    for j in range(1,i):
        print("*",end=" ")
    print(" ")

#while loop:- repaet code block as long as condition stays true.
count=0
while count < 3:
    print("python")
    count+=1

c=1
while c<5:
    print(c)
    c+=1

#infinite loop    
while True:
    print("Welcome") 
    
       


