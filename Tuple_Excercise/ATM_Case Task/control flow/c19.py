cp=float(input("enter cost price:"))
sp=float(input("enter selling price:"))
if sp>cp:
    profit=sp-cp
    print("profit=",profit)
elif cp>sp:
    loss=cp-sp
    print("loss:",loss)
else:
    print("mo profit no loss")        