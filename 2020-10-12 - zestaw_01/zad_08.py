given_num = int(input("Podaj liczbę: "))

div_sum = 0
i = 1

while i <= given_num // 2:
    if given_num % i == 0:
        div_sum += i
    i += 1

if given_num == div_sum:
    print("Jest liczbą doskonałą")
else:
    print("Nie jest liczbą doskonałą")