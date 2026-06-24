from functools import reduce
a=[25,80,15,100,45]
print(reduce(lambda x,y:x if x>y else y,a))