try:
    t1=(1,2,5,3,4,6)
    ind=int(input("enter :"))
    print(t1[ind])
except IndexError:
    print("invalid index")    