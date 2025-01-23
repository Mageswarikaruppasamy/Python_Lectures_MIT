#nummber of vowels and consonants
def func(s):
    vow = 'aeiou'
    v = 0
    c = 0
    for i in s:
        if i in vow:
            v += 1
        else:
            c += 1
    return(v,c)
print(func('hello'))