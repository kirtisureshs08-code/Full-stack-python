try:
    l1=[10,20,30,40,50]
    s=int(input("enter num to remove:"))
    print(l1.remove(s))
    print(l1)
except ValueError:
    print("invalid indices")    
