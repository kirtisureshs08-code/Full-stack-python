def flatten(l1):
    result=[]
    for i in l1:
        if type(i)==l1:
            result.extend(i)
        else:
            result.append(i)
    return result
print(flatten([1,[2,3],4]))
            