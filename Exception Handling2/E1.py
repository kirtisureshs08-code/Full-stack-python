try:
    ch=int(input("enter choice:"))
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    if ch==1:
        print("Result:",a+b)
    elif ch==2:
        print("Result:",a-b)
    elif ch==3:
        print("Result:",a*b)
    elif ch==4:
        print("Result:",a/b)
    else:
        print("invalid choice")
except ValueError:
    print("enter valid ch")
except ZeroDivisionError:
    print("do not divided by zero")            
