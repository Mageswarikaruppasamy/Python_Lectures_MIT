x = float(input("Enter a number: "))
g = x/2
while abs(g**2 - x) >= 0.01:
    g = g - (((g**2) - x)/(2*g))
print(g, "is close to the square root of", x)