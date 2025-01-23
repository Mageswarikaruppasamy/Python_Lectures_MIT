def is_even(i):
    return i % 2 == 0
print(is_even(3))
print(is_even(4))

def div_by(n ,d):
     return n%d == 0
print(div_by(10, 3))
print(div_by(195, 13))

for i in range(1,11):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

def sum_odd(a ,b):
    sum = 0
    for i in range(a,b+1):
        if not is_even(i):
            sum += i
    return sum
print(sum_odd(1, 10))

def sum_even(a ,b):
    sum = 0
    while a <= b:
        if is_even(a):
            sum += a
        a += 1
    return sum
print(sum_even(2, 4))

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("hello"))
print(is_palindrome("radar"))
print(is_palindrome("222"))