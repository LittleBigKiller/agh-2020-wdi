# Napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona w precyzji do 0.0001

precision = 0.0001

given_number = float(
    input("Podaj liczbę całkowitą do wyciągnięcia pierwiastka: "))

def root_nr(a, prec):
    x = a / 2

    while abs(a / (x * x) - x) > prec:
        x = (x + (a / (x * x))) / 2
    
    return x

print(root_nr(given_number, precision))
