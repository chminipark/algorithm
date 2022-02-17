import itertools

dwarf = [int(input()) for _ in range(9)]

for i in itertools.combinations(dwarf, 7):
    if sum(i) == 100:
        for j in sorted(list(i)):
            print(j)
        break
