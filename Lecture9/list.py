def sum_mul(L):
    sum = 0
    mul = 1
    for i in L:
        sum += i
        mul *= i
    return (sum,mul)

print(sum_mul([1,2,3]))