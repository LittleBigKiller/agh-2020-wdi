search_for = int(input("Podaj szukany iloczyn: "))

fib = [0, 1]

prev = 0
last = 1
elem = 1

hard_limit = 1000000

while elem < hard_limit:
    fib.append(elem)
    prev = last
    last = elem
    elem = prev + last

for i in range(0, len(fib) - 2):
    il = fib[i] * fib[i+1]
    if il > search_for:
        print("Nie jest")
        quit()
    elif il == search_for:
        print("Jest")
        quit()
