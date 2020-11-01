podana = input("Podaj liczbę całkowitą: ")

try:
    podana = int(podana)
except:
    print(podana + " nie jest liczbą całkowitą, kończenie programu")
else:
    def A(n):
        return n * n + n + 1

    tabela_wartosci = []

    i = 1
    while A(i) < podana:
        tabela_wartosci.append(A(i))
        i += 1

    # print(tabela_wartosci)

    for wartosc in tabela_wartosci:
        if podana % wartosc == 0:
            print(podana, " jest wielokrotnością ", wartosc)


