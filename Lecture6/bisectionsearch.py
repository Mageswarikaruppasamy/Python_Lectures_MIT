x = float(input("Enter a number: "))
epsilon = 0.01
numguess = 0
if x <= 1:
    low = x
    high = 1
else:
    low = 0
    high = x
guess = (low+high)/2.0
while abs(guess**2-x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    numguess += 1
print("numguess=", numguess)
print(guess, "is close to the square root of", x)