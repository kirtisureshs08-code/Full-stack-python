class Bankaccount:
    def __init__(self):
        self.__balance=10000
    def deposit(self,amount):
        self.__balance+=amount  
        print("Deposited:",amount)

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdraw:",amount)
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("balance:",self.__balance)
b=Bankaccount()
b.deposit(5000)
b.withdraw(2000)
b.show_balance()                         
