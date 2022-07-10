def flatten(list_of_lists: list) -> list:
    list_flat = []
    for i in list_of_lists:
        list_flat += i
    return list_flat

print(flatten([[1,2],[3,4],[5,6]]))