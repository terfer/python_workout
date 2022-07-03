import json
from os import listdir


def print_scores(dir_name: str):
    files = listdir(dir_name)
    for q in files:
        print(f'{dir_name}/{q}')
        print(score_from_json(f'{dir_name}/{q}'))


def score_from_json(path: str) -> str:
    with open(path) as file:
        s = json.loads(file.read())
    min = [100, 100, 100]
    max = [0, 0, 0]
    average = [0, 0, 0]
    for p, i in enumerate(s):
        for j, k in i.items():
            if j == 'math':
                if k < min[0]:
                    min[0] = k
                if k > max[0]:
                    max[0] = k
                average[0] += k
                if p == (len(s)-1):
                    average[0] = average[0]/(p+1)
            elif j == 'literature':
                if k < min[1]:
                    min[1] = k
                if k > max[1]:
                    max[1] = k
                average[1] += k
                if p == (len(s)-1):
                    average[1] = average[1]/(p+1)
            elif j == 'science':
                if k < min[2]:
                    min[2] = k
                if k > max[2]:
                    max[2] = k
                average[2] += k
                if p == (len(s)-1):
                    average[2] = average[2]/(p+1)

    return f"\tmath: min {min[0]}, max {max[0]}, average {average[0]}\n\tliterature: min {min[1]}, max {max[1]}, average {average[1]}\n\tscience: min {min[2]}, max {max[2]}, average {average[2]}"


print_scores('scores')
