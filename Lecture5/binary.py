x = int(input('Enter an integer: '))
result = ''
negflag = False
if x < 0:
    negflag = True
    x = abs(x)
elif x == 0:
    result = 0
while x > 0:
    result = str(x%2) + result
    x = x//2
if negflag:
    result = '-' + result
print(result)
