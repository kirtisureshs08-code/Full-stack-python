def char_frequency(s):
    for i in set(s):
        print(i,":",s.count(i))
char_frequency("python")        