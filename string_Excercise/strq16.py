s=input("Enetr string:")
words=s.split()
longest=words[0]
for word in words:
    if len(word)>len(words):
        longest=word

print("longest word=",word)        