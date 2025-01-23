def even(n):
    return n % 2 == 0

def five(n):
    return n == 0

def apply(criteria,n):
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count

how_many = apply(even,10)
print(how_many)
how_many = apply(five,10)
print(how_many)