def solution(progresses, speeds):
    pro = progresses
    spe = speeds
    answer = []
    releaseCount = 0

    def checkRelease():
        nonlocal pro, spe, answer, releaseCount

        for i in range(len(pro)):
            if pro[i] >= 100: 
                releaseCount += 1
            else:
                break
        
        if releaseCount != 0:
            del pro[:releaseCount]
            del spe[:releaseCount]
            answer.append(releaseCount)

        releaseCount = 0

    while len(pro) != 0:
        pro = [pro[i] + spe[i] for i in range(len(pro))]
        checkRelease()
    
    return answer

p = [93, 30, 55]
s = [1, 30, 5]

sol = solution(p, s)
print(sol)
