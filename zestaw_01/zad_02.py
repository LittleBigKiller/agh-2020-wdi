search_for = int(input("Podaj szukaną sumę: "))

fib = [0, 1]

prev = 0
last = 1
elem = 1

hard_limit = 1000000

saved_index = 0

while elem < hard_limit:
    fib.append(elem)
    prev = last
    last = elem
    elem = prev + last

    if elem <= search_for:
        saved_index = len(fib) - 1

# print(fib)
# print(fib[saved_index])

if fib[saved_index] == search_for:
    print("Istnieje")
else:
    sum = fib[saved_index]
    current_index = saved_index - 1

    while sum < search_for:
        sum += fib[current_index]
        current_index -= 1
        # print(sum)
    
    if sum == search_for:
        print("Istnieje")
    else:
        print("Nie istnieje")  