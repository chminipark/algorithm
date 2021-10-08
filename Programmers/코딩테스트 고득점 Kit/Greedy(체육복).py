def solution(n, lost, reserve):
    nothave = [i for i in lost if i not in reserve]
    canlend = [i for i in reserve if i not in lost]
    countplus = 0
    countminus = 0
    print(nothave)
    print(canlend)


    for i in reserve:
        if i+1 in lost:
            countplus += 1
    for i in reserve:
        if i-1 in lost:
            countminus += 1
    if n-countplus > n-countminus:
        return n-countplus
    else:
        return n-countminus

# 다시풀기 ..
lost = [2,4]
reserve = [1,3,5]
n = 5
print(solution(n, lost, reserve))