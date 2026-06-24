class Payment:
    def payment(self):
        pass
class Credit(Payment):
    def payment(self):
        print("payment made using credit cart ")  
class Upi(Payment):
    def payment(self):
        print("payment made using upi")
class Netbank(Payment):
    def payment(self):
        print("payment made using netbank")
payments=[Credit(),Upi(),Netbank()]
for p in payments:
    p.payment()

        