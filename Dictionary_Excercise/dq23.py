d={'a':10,'b':20,'c':10,'d':40,}
for value in set(d.values()):
    if list(d.values()).count(value)>1:
        print(value)


    
