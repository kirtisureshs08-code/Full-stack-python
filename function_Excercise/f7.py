def vowels(s):
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    print(count)
print(vowels("kirtika"))            
