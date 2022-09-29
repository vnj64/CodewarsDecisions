def tower_builder(n_floors):
    result = []
    for i in range(n_floors):
        n_floors -= 1
        result.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)


    return result

print(tower_builder(3))