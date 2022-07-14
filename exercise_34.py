def get_sv(filename: str) -> set:
    d = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as file:
        for i in file.readlines():
            for j in i.split():
                if vowels < set(j):
                    d.add(j)
    return d


print(get_sv('dict_file.txt'))
