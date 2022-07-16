from string import ascii_lowercase


def generate_dict_gematria() -> dict:
    return {char: index + 1 for index, char in enumerate(ascii_lowercase)}
