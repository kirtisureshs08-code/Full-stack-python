l1=[2,3,4,5,6]
search=int(input("Enter search num: "))
i=0
while i<len(l1):
    if l1[i]==search:
        print("num found")
        break
    i=i+1
if i==len(l1):
    print("num not found")    