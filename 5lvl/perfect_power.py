from math import sqrt

def isPP(n):
    if int(sqrt(n)) != None:
        counter = 2
        list_of_sqrt = []
        if n % sqrt(n) == 0:
            list_of_sqrt.append(int(sqrt(n)))
        else:
            return None
        if int(sqrt(n)) ** counter == n:
            list_of_sqrt.append(counter)
            return list_of_sqrt
        else:
            counter+=1
    else:
        while n != 2:
            counter_delen = 0
            if n % 2 == 0:
                counter_delen += 1
                n = n // 2



print(isPP(8))