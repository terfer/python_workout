from operator import add, sub, mul, pow, mod, truediv


def cast_input_to_solve(to_cast: str):
    return to_cast.split()[0], float(to_cast.split()[1]), float(to_cast.split()[2])


def calc(to_solve: str):
    operations = {'+': add,
                  '-': sub,
                  '*': mul,
                  '/': truediv,
                  '**': pow,
                  '%': mod}
    operation, first_item, second_item = cast_input_to_solve(to_solve)

    return operations[operation](first_item, second_item)

print(calc("/ 3 50"))