def anagram(str_1, str_2):
    str_1 = list(str_1)
    str_2 = list(str_2)
    str_1 = str_1.sort()
    str_2 = str_2.sort()
    return str_1 == str_2

print(anagram("липа", "пила"))