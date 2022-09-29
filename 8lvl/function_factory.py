def function_factory(x,y,o):
    def result():
        if o == '+':
            return x+y
        elif o == '-':
            return x-y
        elif o == '*':
            return x*y
        elif o == '/':
            return x/y
        else:
            return x%y
    return result