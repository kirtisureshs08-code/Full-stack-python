def get(d,key):
    try:
        return d[key]
    except KeyError:
        return "key not found"
print(get({"name":"neha"},"age"))    