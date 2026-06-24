try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    if not any(ch.isdigit() for ch in password):
        raise ValueError("Password must contain at least one digit.")

    if not any(ch.isupper() for ch in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    print("Password is valid.")

except ValueError as e:
    print(e)