from exercise_5 import pig_latin

def pl_sentence(sentence: str) -> str:
    pl_sentence = ""
    for i in sentence.split(' '):
        pl_sentence += pig_latin(i) + " "
    return pl_sentence

# print(pl_sentence(input("Write a sentence: ")))