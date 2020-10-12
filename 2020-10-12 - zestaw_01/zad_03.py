# Napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona w precyzji do 0.0001

precision = 0.0001

given_number = float(
    input("Podaj liczbę całkowitą do wyciągnięcia pierwiastka: "))

def root_nr(a, prec):
    x = 1
    x_1 = a

    while abs(x - x_1) >= prec:
        x = (x + x_1) / 2
        x_1 = a / x
    
    return x

print(root_nr(given_number, precision))
