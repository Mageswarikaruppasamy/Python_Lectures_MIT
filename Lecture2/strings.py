#string concatenation
b = ":"
c = ")"
s1 = b + 2*c
print(s1)

f = "a"
g =" b"
h = "3"
s2 = (f+g)*int(h)
print(s2)

#string length
print(len(s2))
print(len(s1))

#string slicing
s = 'abcdefgh'
print(s[0:4])
print(s[3:6])
print(s[0:4:2])
print(s[::-1])
print(s[4:1:-2])
s ='ABC d3f ghi'
print(s[3:len(s)-1])
print(s[4:0:-1])
print(s[6::3])

#input & output
#t = input("Enter any verb:")
#print("I can",t,"better than you.")
#print((t+' ')*5)

#fstring
num = 3000
div = 1/3
print(f'{num*div} is a fraction of {div*100}% of {num}')