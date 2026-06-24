sal=float(input("enter the salary:"))
year=int(input("enter years of service:"))
if year>5:
    bonus=sal*0.05
    print("bonus:",bonus)
    print("total salary:",sal+bonus)
else:
    print("no bonus")
    print("total salary:",sal)    
