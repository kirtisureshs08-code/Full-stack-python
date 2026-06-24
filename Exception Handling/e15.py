try:
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    mobile = input("Enter mobile number: ")

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    if "@" not in email:
        raise ValueError("Invalid email.")

    if len(mobile) != 10 or not mobile.isdigit():
        raise ValueError("Invalid mobile number.")

    print("Registration successful.")

except ValueError as e:
    print(e)