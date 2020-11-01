a_1 = float(input("Podaj a_1: "))
b_1 = float(input("Podaj b_1: "))
a_2 = float(input("Podaj a_2: "))
b_2 = float(input("Podaj b_2: "))

print("(", a_1, " + i * ", b_1, ") + (", a_2, " + i * ", b_2, ") = ", a_1 + a_2, " + i * ", b_1 + b_2)
print("(", a_1, " + i * ", b_1, ") - (", a_2, " + i * ", b_2, ") = ", a_1 - a_2, " + i * ", b_1 - b_2)

print("(", a_1, " + i * ", b_1, ") * (", a_2, " + i * ", b_2, ") = ", a_1 * a_2 - b_1 * b_2, " + i * ", (a_1 * b_2 + a_2 * b_1))
print("(", a_1, " + i * ", b_1, ") : (", a_2, " + i * ", b_2, ") = ", (a_1 * a_2 + b_1 * b_2) / (a_2 ** 2 + b_2 ** 2), " + i * ", (a_2 * b_1 - a_1 * b_2) / (a_2 ** 2 + b_2 ** 2))
