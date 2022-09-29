def beeramid(bonus, price):
    number_we_can_afford = bonus // price
    level = 0

    while ((level+1)**2 <= number_we_can_afford):
        level += 1
        number_we_can_afford -= level*level

    return level

print(beeramid(1500, 2))