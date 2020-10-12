given_num = 2 # Nie udowodniono istnienia nieparzystych liczb doskonałych

while given_num < 1000000:
    div_sum = 0
    i = 1

    while i <= given_num // 2:
        if given_num % i == 0:
            div_sum += i
        i += 1

    if given_num == div_sum:
        print(given_num)

    given_num += 2 # Nie udowodniono istnienia nieparzystych liczb doskonałych

    if given_num == 8130:
        print("Wszystkie znalezione, dalej już tylko czekanie aż doliczy do miliona... Polecam Ctrl+C tbh")
        # Na prawdę nic tam dalej nie ma, następna liczba doskonała to 33 550 336