def solution(n):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    print(numbers.items())
    for k, v in numbers.items():
        for i in n:
            if k == i:
                output += v
    return output

print(solution('MCMLXXXIX'))