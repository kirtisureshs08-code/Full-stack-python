l1=['a','b','c']
d={}
for i in l1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1    
print(d)