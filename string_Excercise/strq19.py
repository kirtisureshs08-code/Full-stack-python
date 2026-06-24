s=input("Enetr string:")
upper=0
lower=0
special=0
for ch in s:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    else:
        special+=1
print("Uppercase Letters:",upper)    
print("lowercase Letters:",lower)     
print("Special Letters:",special)     


    