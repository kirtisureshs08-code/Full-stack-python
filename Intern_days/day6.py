# Tuple:-tuple is ordered collection which is immutable .denoted by ().tuple is read 
# only version of list
'''t1=()
print(type(t1))

t2=("kirti",2.3,True,45,[1,2,3],0)
print(len(t2)) 

#the single value stored in tuple i.e seperated by (,) mean when we want to get
#  the type tuple so used ,
t=(1,)
print(type(t))

print(t2[::-1])

#convert tuple into list
l1=list(t2)
print(l1)

#convert list into tuple
t2=tuple(l1)
print(t2)

print(t2[-6:-3])

# range function (start value,End value+1,step value)
#table of 5
for i in range(5,50+1,5):
    print(i)

#table of 7
t3=tuple(range(7,71,7))
print(t3)

#addition &multi op for tuple
t4=(1,2,3)
t5=(4,5,6)
t6=t4+t5 # '+' concatination
print(t6)

print(t4 * 5)  # '*' repetation op

#count function: returns the no of occerence of given element in tuple
t7=(1,2,3,4,5,4,6)
print(t7.count(4))

#max function: largest value
print(max(t7))

#min function: smallest value
print(min(t7))

#index function: retuns 1st occ of given element in tuple
t=(10,20,30,40,50)
print(index(30))

#sorted function: this used to sort the element based on default  natural (ascending & descending)
t.sorted(t,reverse=True)   #descending
print(t)

#tuple (packing & unpacking)
a=10
b=20
c=30
d=40
tuple=a,b,c,d
print(tuple)   #tuple packing

t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)  #tuple unpacking


#list comprehension is a concise way to create new lists in python by applying an expression to each item in an existing list
syntax:- new list:[expression]
#tuple comprehension does not exist.

marks=[20,30,40,50,60]
new_marks=[]
for x in marks:
    new_marks.append(x+2)
print(new_marks)    


#wAP list of even and odd num in list using list_com
#WAP to ask the user to enter names of their 3 fav movies and store them tuple
m1=input("Enter the 1 fav movie names:")
m2=input("Enter the 1 fav movie names:")
m3=input("Enter the 1 fav movie names:")

tuple1=m1,m2,m3
print(tuple1)   

#set are unorderd collection that automatically remove duplicates. denoted by {}
s1={1,"kirti",2.5,True,0,False}
print(s1)    '''

l1=[10,20,30,40]
s2=set(l1)
print(s2)

l2=('kirti',2.4,5)
s3=set(l2)
print(s3)

#add item in list
s={10,20,30,40}
s.add(80)
print(s)

#update
s2={"a","b","c"}
s.update(s2)
print(s)

#remove
s.remove("a")
print(s)