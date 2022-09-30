def find_outlier(integers):
    list_even = []
    list_odd = []
    for number in integers:
        if number % 2 == 0:
            list_even.append(number)
        else:
            list_odd.append(number)
    
    if len(list_odd) == 1:
        for number in list_odd:
            return number
    else:
        for number in list_even:
            return number
        
print(find_outlier([1, 3, 5, 7, 9, 2]))