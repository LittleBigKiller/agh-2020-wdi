given_num_0 = int(input("Podaj pierwszą liczbę: "))
given_num_1 = int(input("Podaj drugą liczbę: "))
given_num_2 = int(input("Podaj trzecią liczbę: "))


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a


def nww(a, b):
    return a * b // nwd(a, b)

print(nww(nww(given_num_0, given_num_1), given_num_2))
