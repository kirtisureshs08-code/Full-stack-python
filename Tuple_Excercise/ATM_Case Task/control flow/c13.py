units=int(input("Enetr number:"))
if units>=100:
    bill=units*2
elif units>=200:
    bil=(100*2)+(units-100)*3
else:
    bill=(100*2)+(100*3)+(units-200)*5
print("electricity bill:",bill)            
    