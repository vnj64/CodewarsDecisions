def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for letter in string_:
        if letter in vowels:
            string_ = string_.replace(letter, '')
    return string_

print(disemvowel('This website is for losers LOL!'))