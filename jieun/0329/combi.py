import itertools
mylist = [1, 2, 3]
result = itertools.combinations(mylist, 2) # r 필수 인자
print(list(result))