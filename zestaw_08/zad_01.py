# Wykorzystując algorytm Euklidesa napisz funkcję wyznaczającą Największy Wspólny
# Dzielnik (NWD) wprowadzonych przez użytkownika liczb. Zwizualizuj w konsoli rekurencyjny
# sposób działania programu.


def is_positive_int(a):
    if a == "":
        return False

    try:
        a = int(a)
    except:
        return False

    if a <= 0:
        return False

    return True


def clear_console():
    print("\033c", end="")


#test


def nwd_euclid(a, b):

    if a < b:       # Funkcja zakłada, że pierwsza z podanych jest większa
        # wywołanie ponowne ze "skorygowanymi" parametrami
        return nwd_euclid(b, a)

    if b != 0:
        # Jeżeli 'b' nie wynoosi 0, to wykonujemy dalszy krok w algorytmie ekulidesa
        print(      # Wizualizujemy krok w algorytmie sformatowanym stringiem
            '{first} = {hmt} * {second} + {diff}'.format(       # Sformatowany string, słowa w '{}' to nazwy zmiennych
                first=a,        # Przypisanie zmiennej odpowiedniej wartości, tutaj pierwszej liczby podanej naszej funkcji
                hmt=a//b,       # Przypisanie całkowitej wartości z dzielenia 'a' przez 'b'
                second=b,
                diff=a % b      # Przypisanie reszty z dzielenia 'a' przez 'b'
            )
        )

        print('Wywołanie funkcji nwd_euclid({0}, {1})'.format(b, a % b))

        # ponowne wywołanie naszej funkcji z nowymi danymi - mniejsza z danych ('b') i reszta z dzielenia danych ('a' przez 'b')
        return nwd_euclid(b, a % b)

    else:
        print('Drugi argument funkcji wynosi 0 - znaleziono NWD')
        # Jeżeli 'b' wynosi 0, to oznacza, że podane funkcji 'a' zawiera wartość NWD pierwotnie podanych liczb
        print('NWD wynosi: {nwd}\n'.format(nwd=a))
        return a


# nwd_euclid(165, 304)
# nwd_euclid(5000, 50)
# nwd_euclid(150, 9)
# nwd_euclid(2310, 13)

clear_console()
print("Format wykonywanej funkcji: NWD(a, b)")

while True:
    a = input("Podaj a: ")
    if is_positive_int(a):
        a = int(a)
        break

    print("Nieprawidłowe dane.")


while True:
    b = input("Podaj b: ")
    if is_positive_int(b):
        b = int(b)
        break

    print("Nieprawidłowe dane.")

print('\nWykonywanie NWD({0}, {1}):\n'.format(a, b))
nwd_euclid(a, b)
