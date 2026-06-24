try:
    a=10
    b=0
    c=a/b
except ZeroDivisionError:
    print("do not diveded by zero")
else:
    print(c)
finally:
    print("always execute")    

