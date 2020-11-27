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


def count_arit_seq(tab):
    count = 0
    current_length = 2
    current_diff = 0

    i = 1
    while i < len(tab):
        if i != 1:
            if tab[i] - tab[i-1] != current_diff:
                if current_length > 2:
                    count += 1

                current_length = 2
                current_diff = tab[i] - tab[i-1]

            else:
                current_length += 1
        else:
            current_diff = tab[i] - tab[i-1]

        i += 1

    if current_length > 2:
        count += 1

    return count


def count_geom_seq(tab):
    count = 0
    current_length = 2
    current_diff = 0

    i = 1
    while i < len(tab):
        if tab[i-1] != 0:
            if i != 1:
                if tab[i] / tab[i-1] != current_diff:
                    if current_length > 2:
                        count += 1

                    current_length = 2
                    current_diff = tab[i] / tab[i-1]

                else:
                    current_length += 1
            else:
                current_diff = tab[i] / tab[i-1]

        else:
            current_length = 2
            current_diff = 0

        i += 1

    if current_length > 2:
        count += 1

    return count


def gen_tab(tl):
    tab = [round(random.uniform(-32768, 32767), 3) for i in range(tl)]

    return tab


def main():
    while True:
        tab_len = input("Podaj długość tablicy: ")
        if is_positive_int(tab_len):
            tab_len = int(tab_len)
            break

        print("Nieprawidłowe dane.")

    tab = gen_tab(tab_len)

    # tab = [2, 1, 0.5, 0.25, 0.5, 1, 1, 1]
    # tab = [1, 1, 1, 1, 0.5, 0.25, 0.5, 0.75, 1, 1.25]
    # tab = [1, 1, 1, 1, 0.5, 0.25, 0.5, 0.75, 1, 1.25, 3.25, 5.25, 7.25]

    LA_count = count_arit_seq(tab)
    LG_count = count_geom_seq(tab)

    print(tab)
    print(LA_count)
    print(LG_count)

    if LA_count > LG_count:
        return 1
    elif LA_count < LG_count:
        return -1
    else:
        return 0


print(main())