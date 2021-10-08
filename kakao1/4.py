import itertools
def solution(n, info):

    # 점수 계산
    def score(l_list):
        nonlocal info
        p_score = 0
        l_score = 0
        for count, z in enumerate(zip(info, l_list)):
            if z[0]<z[1] and z[1]:
                l_score += 10-count
            elif z[0]>=z[1] and z[0]:
                p_score += 10-count
        return (p_score, l_score)

    t = [i for i in range(0,11)]
    answer = []
    max_diff = float('-inf')

    for i in itertools.combinations_with_replacement(t, n):
        l_list = [0]*11
        for j in i:
            l_list[10-j] += 1
        p_score, l_score = score(l_list)
        if p_score < l_score:
            diff = l_score - p_score
            if max_diff < diff:
                max_diff = diff
                answer.clear()
                answer.append(l_list)
            elif max_diff == diff:
                answer.append(l_list)

    if answer:
        return max(answer, key= lambda x : x[-1])
    else:
        return [-1]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
solution(n, info)

l_list=[0,0,0,0,0,0,0,0,0,0,0]
def score(l_list,info):
    p_score = 0
    l_score = 0
    for count, z in enumerate(zip(info, l_list)):
        print(count, z)
        if z[0]<z[1] and z[1]:
            l_score += 10-count
        elif z[0]>=z[1] and z[0]:
            p_score += 10-count
    return (p_score, l_score)
print(score(l_list,info))

a = [1]
a.count(1)

a = [1,2,3]
b = [4,5,6]
for x,y,z in enumerate(zip(a,b)):
    print(x)
    print(y)
    print(z)