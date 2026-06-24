try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width

    print("Area =", area)

except ValueError:
    print("Invalid numeric value.")