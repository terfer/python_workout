from exercise_35a import generate_dict_gematria

def gematria_for(word: str) -> int:
    dict_gematria = generate_dict_gematria()
    score = 0
    for i in word:
        score += dict_gematria.get(i, 0)
    return score

def gematria_equal_words(word: str) -> list:
    score = gematria_for(word.lower())
    return [word_in_sentence for sentence in open('dict_file.txt').readlines() for word_in_sentence in sentence.strip().split() if gematria_for(word_in_sentence.lower()) == score]

print(gematria_equal_words('test'))