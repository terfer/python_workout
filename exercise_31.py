from exercise_6 import pl_sentence

def plword(filename: str) -> str:
    with open(filename, 'r') as file:
        return ' '.join([pl_sentence(x.replace(',','')) for sentence in file.readlines() for x in sentence.replace('\n','').split(' ')  if x.isdigit() == False])


print(plword("file_31"))