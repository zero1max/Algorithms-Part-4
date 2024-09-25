# Task 8

def ishora(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

son = int(input('x: '))
natija = ishora(son)
print(natija)