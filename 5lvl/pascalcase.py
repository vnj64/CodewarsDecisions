import string

def to_underscore(stroka):
    upper_letters = string.ascii_uppercase
    for letter in stroka:
        if letter.is_upper():
            letter = letter.lower()

print(to_underscore("TestController"))