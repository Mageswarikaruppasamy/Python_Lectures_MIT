def square(L):
    for i in range(len(L)):
        L[i] = L[i]**2
    return L
print(square([1,2,3,4,5]))