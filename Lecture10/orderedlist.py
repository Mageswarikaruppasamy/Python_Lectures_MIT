def order_list(n):
    l = []
    for i in range(n+1):
        l.append(i)
    return l

print(order_list(5))

def remove(L,e):
    new = []
    for i in L:
        if i != e:
            new.append(i)
    return new

print(remove([1,2,3,4,5],3))
print(remove([1,6,3,6,5],6))
print(remove([1,2,3,4,5],7))