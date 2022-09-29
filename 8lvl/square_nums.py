def square_sum(numbers):
    counter = 0
    for i in range(len(numbers)):
        counter += numbers[i]**2
    return counter

print(square_sum([1, 2, 2]))