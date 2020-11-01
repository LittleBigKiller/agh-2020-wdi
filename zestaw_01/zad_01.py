print(0)
print(1)

prev = 0
last = 1
elem = 1

hard_limit = 1000000

while (elem < hard_limit):
    print(elem)
    prev = last
    last = elem
    elem = prev + last
    