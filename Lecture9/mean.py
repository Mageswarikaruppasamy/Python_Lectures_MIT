def mean(*args):
    tot = 0
    for i in args:
        tot += i
    return tot/len(args)
print(mean(1,2,3,4,5,6))
print(mean(1,2))