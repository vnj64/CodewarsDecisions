def greetings(time, name):
    if time == None or name == None:
        return "Hey dude greet someone"
    else:
        return "Good {} {}".format(time, name)
print(greetings('evening', 'John'))