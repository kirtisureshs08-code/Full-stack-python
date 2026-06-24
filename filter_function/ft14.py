from functools import reduce
words=["python","is","awesome"]
sentence=reduce(lambda x,y:x+" "+y,words)