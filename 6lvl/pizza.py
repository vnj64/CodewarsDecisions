def which_pizza(d1,price1,d2,price2):
    if d1//price1 > d2//price2:
        return d1
    else:
        return d2

print(which_pizza(40, 9, 20, 4))