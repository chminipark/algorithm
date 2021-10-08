def solution(array, commands):
    answer = []
    ar = array
    cm = commands

    def solK(ar, cm):
        sl = ar[cm[0]-1:cm[1]]
        sl.sort()
        return sl[cm[2]-1]
    
    for i in cm:
        sol = solK(ar, i)
        answer.append(sol)
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

sol = solution(array, commands)
print(sol)