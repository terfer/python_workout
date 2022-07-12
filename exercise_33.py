def transform_values(func_lambda, dictionary: dict) -> dict:
    return {x: func_lambda(y) for x, y in dictionary.items()}


d = {'a': 1, 'b': 2, 'c': 3}

print(transform_values(lambda x: x*x, d))
