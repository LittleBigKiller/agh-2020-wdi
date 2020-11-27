# Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która
# policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o
# długości większej niż 2. Funkcja powinna zwrócić wartość 1 gdy LA>LG, wartość
# −1 gdy LA<LG oraz 0 gdy LA=LG.

import random


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


def gen_tab(tl):
    # tab = [round(random.uniform(-32768, 32767), 3) for i in range(tl)]
    tab = [round(random.uniform(0, 5), 1) for i in range(tl)]

    return tab


def find_all_arithm(tab):
    tab.sort()
    # print(tab)

    i = 0
    c = i
    curr_diff = round(tab[i] - tab[i+1], 5)
    curr_len = 1
    total = 0
    # print(curr_diff)

    while i < len(tab) - 2:
        for j in range(i + 1, len(tab)):
            if tab[c] - tab[j] == curr_diff:
                curr_len += 1
                c = j

            if curr_len > 2:
                total += 1

        curr_len = 1

        i += 1
        c = i

    return total


def find_all_geom(tab):
    tab.sort()
    # print(tab)

    i = 0
    while tab[i] == 0:
        i += 1
    c = i
    while tab[c+1] == 0:
        c += 1
    curr_diff = round(tab[i] / tab[c+1], 5)

    curr_len = 1
    total = 0
    # print(curr_diff)

    while i < len(tab) - 2:
        for j in range(i + 1, len(tab)):
            if tab[j] != 0:
                if tab[c] / tab[j] == curr_diff:
                    curr_len += 1
                    c = j

                if curr_len > 2:
                    total += 1

        curr_len = 1

        i += 1
        while tab[i] == 0:
            i += 1
        c = i

    return total


def main():
    while True:
        tab_len = input("Podaj długość tablicy: ")
        if is_positive_int(tab_len):
            tab_len = int(tab_len)
            break

        print("Nieprawidłowe dane.")

    tab = gen_tab(tab_len)

    # tab = [2, 4, 4, 1, 3]
    # tab = [1, 1, 1, 1, 1]
    # tab = [0.25, 0.5, 1, 2, 2, 2]

    tab.sort()

    print(tab)

    LA_count = find_all_arithm(tab)
    LG_count = find_all_geom(tab)

    print(LA_count)
    print(LG_count)

    if LA_count > LG_count:
        return 1
    elif LA_count < LG_count:
        return -1
    else:
        return 0


print(main())
