class Atm:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def check_balance(self,pin):
        if pin==self.__pin:
            print("Balance:",self.__balance)   
        else:
            print("Incorrect pin")
a=Atm(1234,10000)
a.check_balance(1234)  
a.check_balance(1234)                