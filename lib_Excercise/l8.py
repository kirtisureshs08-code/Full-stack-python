late_days=int(input("Enter late days:"))
member=input("premimum/regular")
fine=late_days*10
if member=="premium":
    fine=fine*0.5
print("fine amount:",fine)