#Checking square root
guess = 0
neg = False
x = int(input("Enter a Number: "))
if x < 0:
    neg = True
while guess**2 < x:
    guess+=1
if guess**2 == x:
    print("Perfect square")
else:
    print("Not a perfect square")
    if neg:
        print("Did you mean",-x,"?")