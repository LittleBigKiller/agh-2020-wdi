# Kod liczy z precyzją do 0.01

def func(x):
    ret = x * x - 2
    return ret

precision = 0.01

tried = 0
lower_bound = 0
higher_bound = 0

while func(tried) < 0:
    lower_bound = tried
    tried += 1
    if func(tried) == 0:
        print(tried)
        quit()

higher_bound = tried

# print(lower_bound)
# print(higher_bound)

i = 0

while (abs(higher_bound - lower_bound) > precision):
    mid_point = (higher_bound + lower_bound) / 2
    new_f = func(mid_point)

    if (new_f < 0):
        lower_bound = mid_point
    elif (new_f > 0):
        higher_bound = mid_point
    else:
        print(mid_point)

    i += 1

# print(lower_bound)
# print(higher_bound)
print((higher_bound + lower_bound) / 2)
