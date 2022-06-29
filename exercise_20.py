def wordcount(filename: str) -> int:
    with open("wcfile.txt", 'r') as f:
        text = f.read()
    n_lines = len(text.split('\n'))
    n_char = len(text)
    n_words = len(text.split(' '))
    n_uwords = len(set(text.split(' ')))
    print(f"Number of lines: {n_lines}")
    print(f"Number of characters: {n_char}")
    print(f"Number of words: {n_words}")
    print(f"Number of unique words: {n_uwords}")


wordcount("wcfile.txt")
