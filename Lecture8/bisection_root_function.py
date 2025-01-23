def bisection_root(x):
    if x <= 1:
        low = x
        high = 1
    else:
        low = 0
        high = x
    epsilon = 0.01
    guess = (low+high)/2.0
    while abs(guess**2 - x) >= epsilon :
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low+high)/2.0
    return guess

'''print(bisection_root(4))
print(bisection_root(9))
print(bisection_root(0.25))
print(bisection_root(123))'''

def count_close_root(n,epsilon):
    count = 0
    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(n - sqrt) < epsilon:
            print(i,sqrt)
            count += 1
        if sqrt > n+1:
            break
    return count

print(count_close_root(10,0.1))
print(count_close_root(100,0.01))