# Task 3

def sumRange(a, b):
    if a>b:
        return 0
    return a+b

a = int(input('a: '))
b = int(input('b: '))
natija = sumRange(a, b)
print(natija)