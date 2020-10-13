given_num_0 = int(input("Podaj pierwszą liczbę: "))
given_num_1 = int(input("Podaj drugą liczbę: "))
given_num_2 = int(input("Podaj trzecią liczbę: "))


def get_divlist(num):
    temp_list = []

    i = 1

    while i * i <= num:
        if num % i == 0:
            temp_list.append(i)
            if num // i != i:
                temp_list.append(num // i)
        i += 1

    temp_list.sort()

    return temp_list


divs_0 = get_divlist(given_num_0)
divs_1 = get_divlist(given_num_1)
divs_2 = get_divlist(given_num_2)

# print(divs_0)
# print(divs_1)
# print(divs_2)

common_multi = list(set(divs_0).union(set(divs_1).union(set(divs_2))))

# print(common_multi)

min_common_multi = 1

for i in common_multi:
    min_common_multi *= i

print(min_common_multi)
