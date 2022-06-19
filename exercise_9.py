import operator

firstlast = operator.itemgetter(0,-1)


print(firstlast((1,2,3,4)))