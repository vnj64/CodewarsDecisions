def likes(names):
    if not names:
        return "no one likes this"
    else:
        if len(names) == 1:
            return f'{names[0] + " likes this"}'
        if len(names) == 2:
            return f'{names[0]}' + " and " + f'{names[1]}' + " like this"
        if len(names) == 3: 
            return f'{names[0]}' + ', ' + f'{names[1]}' + " and " + f'{names[2]}' + " like this"
        if len(names) > 3:
            return f'{names[0]}' + ', ' + f'{names[1]}' + " and " + f'{len(names)-2}' + " others like this"

print(likes(["Peter", "Jacob", "Max", "Kamil"]))