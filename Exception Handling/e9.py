try:
    l1=list(map(int,input("enter list").split()))
    print(max(l1))
except ValueError:
    print("invalid input")    

