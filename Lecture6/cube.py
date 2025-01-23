cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (low+high)/2.0
while abs(guess**3-cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
print(guess, "is close to the cube root of", cube)