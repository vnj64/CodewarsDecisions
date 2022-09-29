from re import L


def find_smallest_int(arr):
    tmp = 0
    for i in range(len(arr)+1):
        if arr[i+1] > arr[i]:
            arr[i] = tmp
        else:
            continue
    return tmp

print(find_smallest_int([34, 15, 88, 2]))