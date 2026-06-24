def sort(d):
    return dict(sorted(d.items(),key=lambda x:x[1]))
print(sort({"a":3,"b":1,"c":3}))