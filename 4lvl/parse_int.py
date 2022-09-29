def parse_int(string):
    singles = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                'seventeen', 'eighteen', 'nineteen']

    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in singles:
            numbers.append(singles.index(token))
        elif token in tens:
            numbers.append((tens.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    
    return sum(numbers)

print(parse_int('seventeen'))