def join_numbers(ran: range) -> str:
    return str([str(x) for x in ran]).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")


numbers = range(150)

print(join_numbers(numbers))
