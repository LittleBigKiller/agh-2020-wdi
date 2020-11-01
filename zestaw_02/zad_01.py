import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b * b - 4 * a * c

# print(delta)

try:
    if delta > 0:
        print("x_1 = ", -b - math.sqrt(delta) / (2 * a))
        print("x_2 = ", -b + math.sqrt(delta) / (2 * a))
    elif delta == 0:
        print("x_0 = ", -b / (2 * a))
    else:
        raise Exception("Delta mniejsza od 0")
except Exception as e:
    print(e)
