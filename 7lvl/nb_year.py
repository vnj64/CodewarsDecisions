def nb_year(p0, percent, aug, p):
    tmp = None
    percent = percent / 100
    quantity = None
    counter = 0
    while quantity != p:
        quantity += ((p0 + p0) * percent) + aug
    return counter

print(nb_year(1000, 2, 50, 1200))