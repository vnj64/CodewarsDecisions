def no_space(x):
    result = ''
    x = x.split()
    for char in x:
        result += char
    return result
print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))