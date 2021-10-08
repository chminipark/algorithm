def solution(N, number):
    prev_Set = {N}
    current_Set = set()
    onlyN = N

    if N == number:
        return 1

    for i in range(2, N+1):
        if int(str(N)*i) == number:
            return i
        else:
            current_Set.add(int(str(N)*i))
        for prev in prev_Set:
            print(prev_Set)
            current_Set.add(prev+N)
            current_Set.add(prev-N)
            current_Set.add(prev*N)
            current_Set.add(prev/N)
        if number in current_Set:
            return i
        else:
            prev_Set = current_Set
            current_Set.clear()
    
    return -1

sol = solution(5, 12)
print(sol)


