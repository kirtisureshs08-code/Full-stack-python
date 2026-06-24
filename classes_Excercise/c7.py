class Bank:
    def __init__(self,ac_no,name,balance):
        self.ac_no=ac_no
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("amount deposite:",amount) 
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdraw amount:",amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("balance:",self.balance)
b=Bank(1001,"kirti",5000)
b.deposit(2000)
b.withdraw(1000)
b.check_balance()                    

