membership=input("Enetr membership(a/ina):")
av_copies=int(input("Enter copies:"))
b_book=int(input("enetr borrow books:"))
if membership=='active' and av_copies>0 and b_book <3:
    print("book issue successfully")
else:
    print("not successfully")    
