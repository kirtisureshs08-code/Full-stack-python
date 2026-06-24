from functools import reduce
numbers=[25,80,15,100,45]
maxium=reduce(lambda x,y: x if x>y else y,numbers)
print("largest Number=",maxium)