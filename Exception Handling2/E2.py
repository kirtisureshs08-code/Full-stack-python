def get(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "invalid index"
print(get([10,20,30]))    