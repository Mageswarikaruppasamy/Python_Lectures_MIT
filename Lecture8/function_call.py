def calc(op,a,b):
    return op(a,b)

def add(a,b):
    return a+b

def div(a,b):
    if b!=0:
        return a/b
    print("The denom was 0.")

result = calc(add,3,2)
print(result)
result = calc(div,2,2)
print(result)