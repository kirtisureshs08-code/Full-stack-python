#Dictionary :- is unorered collection .pairs of keys and values.shown by {}
#features: mutable,fast data access,unique keys,mixed type values
dict={1:"python",2:"java"}
dict1={'name':'sumago infotech','address':['Nashik']}
print(dict1)
print(dict1['name'])
print(dict1['address'])
print(dict1['address'][0])
print(len(dict1))

#nested Dictionary:
data={1:'raj',2:{'a':'python','b':'css'}}
print(data[2]['a'])
data['price']=200  #add new key -value
print(data)
dict1['address']='Nashik'  #update value
print(dict1)

#Methods:
#get():syntax:dict1.get(key)

print(dict1.get('name'))
print(dict1.keys())
print(dict1.values())
print(dict1.copy())
print(dict1.items())
dict1.update(data)
print(dict1)
