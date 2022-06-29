def mysum(*arg):
    if not arg:
        return arg
    sum = arg[0]
    for i in arg:
        sum += i
    return sum
