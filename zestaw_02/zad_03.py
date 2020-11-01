def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return a


def check_fib(n):
    c = 1
    while fib(c+1) <= podana:
        c += 1

    fib_list = []

    for i in range(1, c):
        for j in range(i, c):
            il = fib_list[i] * fib_list[j]
            if il == n:
                print("Podana liczba jest iloczynem wyrazów: %d * %d" % (fib_list[i], fib_list[j]))
                return True

        print("Podana nie jest iloczynem dwóch wyrazów")
        return False


rep = True
while rep:
    try:
        podana = int(input("Podaj liczbę naturalną: "))
    except:
        print("Wprowadzono niepoprawną wartość.")
    else:
        rep = False

check_fib(podana)
