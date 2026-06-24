s=input("Enter string:")
for ch in s:
    if ch.isupper():
        print(ch.lower(),end="")
    elif ch.lower():
        print(ch.upper(),end="")
    else:
        print(ch,end="")        