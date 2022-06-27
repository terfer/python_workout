numbers = [1, 2, 3, 1, 2, 3, 4, 1]

def how_many_different_numbers(num : list):
    return len(set(num))

print(how_many_different_numbers(numbers))