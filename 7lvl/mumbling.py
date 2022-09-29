def accum(c):
    result = ''
    for i in range(len(c)):
        result += (c[i])*(i+1) + '-'
    return result[:-1].title()

print(accum("abcd"))