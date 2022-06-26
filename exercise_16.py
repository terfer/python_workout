d1 = {'a':1 , 'b':2, 'c':3}
d2 = {'a':1 , 'b':2, 'c':4}
d3 = {'a':1 , 'b':2, 'd':3}
d4 = {'a':1 , 'b':2, 'c':4}
d5 = {'a':1 , 'b':2, 'd':4}

def dictdiff(d1: dict, d2: dict) -> dict:
    dict_sol = {}
    for i,j in zip(d1.keys(),d1.values()):
        if not d2.get(i):
            dict_sol[i] = [j, None]
        elif d2.get(i) != j:
            dict_sol[i] = [j, d2.get(i)]
    for i,j in zip(d2.keys(),d2.values()):
        if not d1.get(i):
            dict_sol[i] = [None, j]
    return dict_sol

print(dictdiff(d1,d1))
print(dictdiff(d1,d2))
print(dictdiff(d3,d4))
print(dictdiff(d1,d5))