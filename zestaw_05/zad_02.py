# Proszę napisać program wczytujący dwie macierze o ustalonych wymiarach mx n.
# Dla wczytanych macierzy należy wykonać operacje: iloczynu dwóch macierzy
# oraz mnożenia przez skalar każdej z tych macierzy, gdzie skalar jest sumą
# wyznaczników wczytanych macierzy.
# Wymiar macierzy powinien być definiowany przez użytkownika.


# region Funkcje Numeryczne
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


def is_number(a):
    if a == "":
        return False
    try:
        a = float(a)
    except:
        return False

    return True
# endregion


# region Tworzenie Matryc
def input_matrix(h, w):
    tab = []
    for i in range(h):
        tab.append([])
        for j in range(w):
            while True:
                print("wiersz: ", i + 1, " - kolumna: ", j + 1)
                x = input("Podaj wartość: ")
                if is_number(x):
                    break

                print("Wartość musi być liczbowa.")

            tab[i].append(float(x))

    return tab

def create_matrix(h, w):
    tab = []
    for i in range(h):
        tab.append([])
        for _ in range(w):
            tab[i].append('')

    return tab
# endregion


# region Wyznaczniki
def can_calc_det(mtx):
    if len(mtx) != len(mtx[0]):
        return False
    return True


def calc_det(mtx):
    if len(mtx) == 1:
        return mtx[0][0]
    if len(mtx) == 2:
        return mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]
    else:
        det = 0
        for i in (range(len(mtx[0]))):
            det += mtx[0][i] * ((-1)**(2+i)) * calc_det(calc_sub_mtx(mtx, i))
        return det


def calc_sub_mtx(mtx, col):
    sub = mtx[1:]
    for i in range(len(sub)):
        sub[i] = sub[i][:col] + sub[i][col+1:]

    return sub


def multiply_matrix_scalar(mtx, sclr):
    tab = mtx[:]
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            tab[i][j] *= sclr

    return tab
# endregion


# region Mnożenie matryc
def can_multiply_matrices(mtx0, mtx1):
    if len(mtx0[0]) != len(mtx1):
        return False
    return True


def multiply_matrices(mtx0, mtx1):
    res = create_matrix(len(mtx0), len(mtx0[0]))
    for i in range(len(mtx0)):
        for j in range(len(mtx1[0])):
            temp = 0
            for k in range(len(mtx0[i])):
                # mtx0_c = mtx0[i][k]
                # mtx1_c = mtx1[k][j]
                temp += mtx0[i][k] * mtx1[k][j]
            res[i][j] = temp

    return res
# endregion


# region input
# tym razem nie tragedia z wczytywaniem!!
while True:
    m0 = input("Podaj m0: ")
    if is_positive_int(m0):
        m0 = int(m0)  # fajnie by było nie musieć tego robić tbh
        break

    print("Nieprawidłowe dane.")

while True:
    n0 = input("Podaj n0: ")
    if is_positive_int(n0):
        n0 = int(n0)
        break

    print("Nieprawidłowe dane.")

while True:
    m1 = input("Podaj m1: ")
    if is_positive_int(m1):
        m1 = int(m1)  # fajnie by było nie musieć tego robić tbh
        break

    print("Nieprawidłowe dane.")

while True:
    n1 = input("Podaj n1: ")
    if is_positive_int(n1):
        n1 = int(n1)
        break

    print("Nieprawidłowe dane.")
# endregion

print("==== Macierz 1: ====")
mtx0 = input_matrix(m0, n0)

print("==== Macierz 2: ====")
mtx1 = input_matrix(m1, n1)

print(mtx0)
print(mtx1)

if can_multiply_matrices(mtx0, mtx1):
    print(multiply_matrices(mtx0, mtx1))
else:
    print("Nie da się pomnożyć macierzy 1 przez macierz 2.")


if can_calc_det(mtx0) and can_calc_det(mtx1):
    sclr = calc_det(mtx0) + calc_det(mtx1)

    print(multiply_matrix_scalar(mtx0, sclr))
    print(multiply_matrix_scalar(mtx1, sclr))
else:
    print("Nie mozna wyliczyć wyznacznika co najmniej jednej z macierzy.")
