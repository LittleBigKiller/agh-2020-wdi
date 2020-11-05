import random


# funkcja zwracająca najdłuższą sekwencję w formie tablicy
def find_longest_sequence(A):
    longest_length = 0  # długość najdłuższej sekwencji
    longest_begin = 0  # indeks początku najdłuższej sekwencji

    current_diff = 0  # różnica r w obecnej sekwencji
    current_length = 2  # długość obecnej sekwencji
    current_begin = 0  # indeks początku obecnej sekwencji

    i = 1
    while i < len(A):
        if i != 1:
            if A[i] - A[i-1] != current_diff:
                if current_length > longest_length:
                    longest_length = current_length
                    longest_begin = current_begin

                current_length = 2
                current_diff = A[i] - A[i-1]
                current_begin = i - 1

            else:
                current_length += 1
        else:
            current_diff = A[i] - A[i-1]

        i += 1

    if current_length > longest_length:
        longest_length = current_length
        longest_begin = current_begin

    end_pointer = longest_begin + longest_length

    return A[longest_begin:end_pointer]


# tragicznie napisane wczytywanie, ale przynajmniej pyta do skutku
repeat = True
while repeat:
    N = input("Podaj długość listy (liczba całkowita dodatnia): ")

    try:
        if N != "":
            N = int(N)
        else:
            N = 0
    except:
        print("Podana nie jest liczbą całkowitą.")
    else:
        repeat = False
        if N <= 0:
            print("Podana liczba nie jest dodatnia.")
            repeat = True

repeat = True
while repeat:
    M = input("Podaj górną granicę (liczba całkowita): ")

    try:
        if M != "":
            M = int(M)
        else:
            M = 0
    except:
        print("Podana nie jest liczbą całkowitą.")
    else:
        repeat = False

repeat = True
while repeat:
    L = input("Podaj dolną granicę (liczba całkowita): ")

    try:
        if L != "":
            L = int(L)
        else:
            L = 0
    except:
        print("Podana nie jest liczbą całkowitą.")
    else:
        repeat = False
        if L > M:
            print("Podana dolna granica jest mniejsza od górnej granicy.")
            repeat = True
# Koniec tragedii

tab = []  # nasza losowana tablica

# wypełnianie tablicy
i = 0
while i < N:
    tab.append(random.randint(L, M))
    i += 1

print("Oryginalna tablica: ", tab)

tab = [0, 0, 0, 1, 2, 3, 4, 5, 0, 1, 2, 0]

longest_seq = find_longest_sequence(tab)

print("Najdłuższa sekwencja: ", longest_seq)

print("Suma: ", sum(longest_seq))
