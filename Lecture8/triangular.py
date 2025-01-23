def is_triangular(n):
    tot = 0
    for i in range(n+1):
        tot += i
        if tot == n:
            return True
    return False
print(is_triangular(6))