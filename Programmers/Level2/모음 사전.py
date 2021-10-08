def solution(word):
    import itertools
    answer = 0
    pedia = set()

    for i in range(1, 6):
        for j in itertools.combinations(['A','E','I','O','U'], i):
            for a in itertools.product(j, repeat = len(j)):
                pedia.add(''.join(a))
    
    pedia = list(pedia)
    pedia.sort()
    answer = pedia.index(word)

    return answer+1

print(solution('AAAAE'))
