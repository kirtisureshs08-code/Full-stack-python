def pass_strength(pwd):
    if len(pwd)>=8:
        return "strong"
    else:
        return "weak"
print(pass_strength("abc12345"))    