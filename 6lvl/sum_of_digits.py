def digital_root(n):
    counter = 0
    for number in n:
        counter += int(number)

    return counter

print(digital_root('123'))