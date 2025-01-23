x = int(input("Enter a number to find square root: "))
epsilon = 0.01
guess = 0.0
increment = 0.00001
num_guess = 0
while abs(guess**2-x) >= epsilon and (guess**2) <= x:
    guess += increment
    num_guess += 1
print('Number of guesses =', num_guess)
if abs(guess**2-x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(guess, 'is close to square root of', x)