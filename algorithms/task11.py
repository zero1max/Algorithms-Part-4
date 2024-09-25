# Task 5

def isSquare(a):   
    if a < 0:
        return False      
    i = 0
    while i * i <= a:
        if i * i == a:
            return True
        i += 1
    return False
b = int(input('a: '))

print(isSquare(b))