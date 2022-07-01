from os import listdir

def find_longest_word(filename: str):
    len_longest_word = 0
    longest_word = ""
    print(filename)
    for i in open(filename, 'r', encoding='UTF-8').read().split():
        if len(longest_word) < len(i):
            len_longest_word = len(i)
            longest_word = i
    return (longest_word, len_longest_word)


def find_all_longest_words(dir: str):
    dict_longest_word = {}
    for i in listdir(dir):
        key, value = find_longest_word(f"{dir}/{i}")
        dict_longest_word[key] = value
    return dict_longest_word

print(find_all_longest_words("exercise_21_books"))