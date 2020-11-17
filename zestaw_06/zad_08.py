# Wykorzystując funkcje, proszę napisać program, który umożliwia dodawanie, odejmowanie i
# mnożenie dwóch plików. Pliki A i B zawierają po 7 słów w kolejnych linijkach, co ważne bez
# powtórzeń w obrębie pliku, między plikami możliwe jest powtarzanie. Dodawanie to
# operacja, w wyniku której tworzony jest plik C zawierający 7 słów w kolejnych linijkach
# zawierający wszystkie słowa z A i B bez powtórzeń tak, że naprzemiennie w kolejnych
# ułożone są słowa występujące tylko w A i B (jeśli występują powtórki umieszczone są na
# końcu pliku). Odejmowanie z kolei to słowa występujące tylko w A a nie w B umieszczone
# bez powtórzeń po 7 w linijce. W wyniku mnożenia tworzony jest plik C, który ma 7 razy
# wpisane powtarzające się słowo w osobnej linii. Słowa są w takim wypadku ułożone
# alfabetycznie. Należy obsłużyć wyjątki.


def purge_endlines(line_list):
    line_list = [x.replace("\n", "") for x in line_list]
    return line_list


def distil_words(line_list):
    line_list = [x.split(" ") for x in line_list]
    return line_list


def sum_list_of_lists(line_list):
    new_list = []
    for line in line_list:
        for word in line:
            new_list.append(word)
    return new_list


def write_seven_words_per_line_to_file(word_list, file_handle):
    write_string = ""
    i = 0
    for word in word_list:
        if i % 7 == 0:
            if i != 0:
                write_string += "\n"
        else:
            write_string += " "

        write_string += word
        i += 1

    file_handle.write(write_string)


def write_each_word_seven_times_to_file(word_list, file_handle):
    write_string = ""
    is_first = True
    for word in word_list:
        for i in range (0, 7):
            if i % 7 == 0:
                if not is_first:
                    write_string += "\n"
            else:
                write_string += " "

            write_string += word
        is_first = False

    file_handle.write(write_string)


def create_addition_wordlist(from_a, from_b):
    repeats = list(set(from_a + from_b) - (set(from_a) - set(from_b)))

    do_a = True
    i_a = 0
    i_b = 0
    new_list = []
    while i_a < len(from_a) or i_b < len(from_b):
        if do_a:
            while i_a < len(from_a) and from_a[i_a] in repeats:
                i_a += 1
            if i_a < len(from_a) and from_a[i_a] not in repeats:
                new_list.append(from_a[i_a])
            i_a += 1
            if i_b < len(from_b):
                do_a = False
        else:
            while i_b < len(from_b) and from_b[i_b] in repeats:
                i_b += 1
            if i_b < len(from_b) and from_b[i_b] not in repeats:
                new_list.append(from_b[i_b])
            i_b += 1
            if i_a < len(from_a):
                do_a = True

    for repeat in repeats:
        new_list.append(repeat)
        new_list.append(repeat)

    return new_list


def clear_console():
    print("\033c", end="")


f_a = open("zestaw_06/a.txt", "r")
f_b = open("zestaw_06/b.txt", "r")
f_c = open("zestaw_06/c.txt", "w")


file_a = distil_words(purge_endlines(f_a.readlines()))
file_b = distil_words(purge_endlines(f_b.readlines()))

# print(file_a)
# print(file_b)

action = ""
action_list = ["0", "1", "2", "3"]

while action not in action_list:
    clear_console()
    print("# # # # # # # # # # # # # #")
    print("#                         #")
    print("#         Akcje:          #")
    print("#      (1) Dodawanie      #")
    print("#     (2) Odejmowanie     #")
    print("#      (3) Mnożenie       #")
    print("#                         #")
    print("#       (0) Zakoncz       #")
    print("#                         #")
    print("# # # # # # # # # # # # # #")
    print("                           ")
    action = input("Wybor akcji: ")

if action == "0":
    f_a.close()
    f_b.close()
    f_c.close()
    exit()

elif action == "1":
    sol_a = sum_list_of_lists(file_a)
    sol_b = sum_list_of_lists(file_b)

    final_list = create_addition_wordlist(sol_a, sol_b)

    write_seven_words_per_line_to_file(final_list, f_c)

    print("Zapisano dodawanie do pliku c.txt")

elif action == "2":
    sol_a = set(sum_list_of_lists(file_a))
    sol_b = set(sum_list_of_lists(file_b))

    final_list = list(sol_a - sol_b)

    final_list.sort()

    write_seven_words_per_line_to_file(final_list, f_c)

    print("Zapisano odejmowanie do pliku c.txt")

elif action == "3":
    sol_a = sum_list_of_lists(file_a)
    sol_b = sum_list_of_lists(file_b)

    final_list = list(set(sol_a + sol_b) - (set(sol_a) - set(sol_b)))

    final_list.sort()

    write_each_word_seven_times_to_file(final_list, f_c)

    print("Zapisano mnożenie do pliku c.txt")


f_a.close()
f_b.close()
f_c.close()
