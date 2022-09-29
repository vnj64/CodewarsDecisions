def consecutive(arr, a, b):
    result = []
    result.append(a), result.append(b)
    for numb in range(0, len(arr)):
        for j in range(len(result)):
            if result[j] == arr[numb] and result[j+1] == arr[numb+1]:
                return True
            else:
                return False
                
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4))
