try:
    num=int(input("Enter num:"))
    print(10/0)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")        
try:
    d={"name":"neha"}
    print(d["age"])
except KeyError:
    print("KeyError")        
try:
    lst=[1,2,3]
    print(lst[5])
except IndexError:
    print("IndexError")    
try:
    print(5+"abc")
except TypeError:
    print("TypeError")            