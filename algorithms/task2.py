import math

def diskriminant(a, b, c):
    D = b**2-4*a*c

    if D>0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        return f"x1: {x1}, x2: {x2}"
    elif D == 0:
        x = (-b+math.sqrt(D))/2*a

        return f"x: {x}"
    else:
        return "Bo'sh to'plam!"

print(diskriminant(1, -2, 1))
