def pick_numbers(string: str) -> list:
    try:
        number = int(string)
        return number
    except:
        return 0

def sum_numbers(mix_string: str) -> float:
    return sum([pick_numbers(x) for x in mix_string.split()])


print(sum_numbers("10 abc 20 de44 30 55fg 40"))
