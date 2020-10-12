given_num = int(input("Podaj liczbę: "))

if given_num % 2 == 0:
    print("Nie jest")
    quit()
else:
    half = given_num // 2
    i = 3
    while (i < half):
        if given_num % i == 0:
            print("Nie jest")
            quit()
        i += 2
    print("Jest")