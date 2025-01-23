#Number of even numbers
even = 0
for i in range(-4,6,2):
    if i%2 == 0:
        even+=1
print("No.of even numbers:",even)

#Number of unique characters
s = "abca"
seen = ''
for i in s:
    if i not in seen:
        seen+=i
print(len(seen))