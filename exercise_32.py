def flip_dict(dict_to_flip: dict) -> dict:
    return {y:x for x,y in dict_to_flip.items()}

print(flip_dict({'a':1, 'b':2, 'c':3}))