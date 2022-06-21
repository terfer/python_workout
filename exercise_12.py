from collections import Counter

words = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_word(words : list):
    word_most_repeated_letter = words[0]
    for i in words:
        if Counter(word_most_repeated_letter).most_common()[0][1] < Counter(i).most_common()[0][1]:
            word_most_repeated_letter = i
    return word_most_repeated_letter

print(most_repeating_word(words))