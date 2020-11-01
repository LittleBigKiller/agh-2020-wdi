fib = [1]

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
    print(fib[i+1] / fib[i])

