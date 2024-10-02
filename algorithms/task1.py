def digit(k, n):
    if len(str(k)) > n:
        return 2
    if len(str(k)) < n:
        return -1


print(digit(12123, 3))
print(digit(12, 3))
