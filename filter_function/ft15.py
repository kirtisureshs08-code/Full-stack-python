from functools import reduce
salary=[25000,30000,28000,35000]
total_sal=reduce(lambda x,y:x+y,salary)
print("total salary:",total_sal)