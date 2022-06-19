def ubbi_dubbi(word: str) -> str:
    ubbi_dubbi_word = ""
    for i in word:
        if i in 'aeiou':
            ubbi_dubbi_word += 'ub'
        ubbi_dubbi_word += i
    return ubbi_dubbi_word

print(ubbi_dubbi(input("Ubbi Dubbi word: ")))