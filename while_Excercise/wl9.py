balance=1000
while True:
     print("1.check balance \n2.withdraw \n3.exit")
     choice=int(input("enter choice:"))
     
     if choice==1:
        print("balance:",balance)
     elif choice==2:
        amount=int(input("Enetr amount:"))
        balance=balance-amount
        print("remaining balance:",balance)  
     elif choice==3:
        break      
