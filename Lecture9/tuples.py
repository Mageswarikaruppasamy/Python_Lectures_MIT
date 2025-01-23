tup = (1,2,'a',3,4,(1,2))
print(tup[0:len(tup)])
print(tup[len(tup)::-1])
print(tup[::-1])
print(tup[5][1])
print(tup[-2:])
print(tup[:-1])
for i in tup:
    print(i)

#swap without extra variable
x = 3
y = 5
z = 10
(x,y,z) = (y,z,x)
print(x,y,z)