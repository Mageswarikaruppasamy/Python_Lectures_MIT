s = 11
found = False
for i in range(11):
    if i == s:
        print("Secret number found")
        found = True
if not found:
    print("Secret number not found")