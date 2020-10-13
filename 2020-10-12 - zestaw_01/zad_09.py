given_num = 1

def div_sum(num):
    div_sum = 0
    i = 1

    while i <= num // 2:
        if num % i == 0:
            div_sum += i
            if num % i != i:
                div_sum += num % i
        i += 1

    return div_sum

while given_num < 1000000:
    # print(given_num)
    pot_pair = div_sum(given_num)
    # print(pot_pair)
    if not given_num >= pot_pair:
        # print(div_sum(pot_pair))
        if given_num == div_sum(pot_pair):
            print(str(given_num) + ", " + str(pot_pair))
    # print("-----")
    # if given_num == 220:
    #     quit()
    
    given_num += 1