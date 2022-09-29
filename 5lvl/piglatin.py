# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.
# Pig latin is cool -> igPay atinlay siay oolcay
# Hello world ! -> elloHay orldway !

def pig_it(text):
    ay = "ay"
    text = text.split(' ')
    for i in text:
        for j in i:
            print(j[i])

print(pig_it('Hello world!'))