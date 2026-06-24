#exception handling:-
#Error:-an unexpected output during the program excution
#try:- actual code
#except:-handles the try block error
#else:-when try block are right else executed
#finally:-always executes

try:
    a=10
    b="sumago"
    c=a+b

except TypeError:
    print("do not add int and string")

#Eg:-
try:
    print("value of z",z)
except NameError:
    print("valiable is not defined")   


#eg:-
try:
    a=int(input("enter 1st num:"))
    b=int(input("enter 1st num:"))
    c=a/b
except ZeroDivisionError:
    print("do not divided by zero")
except ValueError:
    print("do not enter symbol, character")
else:
    print(c)
finally:
    print("always executed")    


#Eg:-
try:
    l1=[1,2,5,6]
    print(l1[4])
except IndexError:
    print("4th index is not available in list")            

#keyError:-
try:
    d={'name':'kirti','age':18}
    print(d['marks'])
except KeyError:
    print("key is not defined")    
