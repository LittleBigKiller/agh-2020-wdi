given_num = int(input("Podaj liczbę: "))

print(1)

i = 2

while i * i <= given_num:
    if given_num % i == 0:
        print(i)
        if given_num // i != i:
            print(given_num // i)
    i += 1
