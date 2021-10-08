def solution(clothes):

    dicClothes = {}
    answer = 1

    for i in clothes:
        if i[1] in dicClothes:
            dicClothes[i[1]].append(i[0])
        else:
            dicClothes[i[1]] = [i[0]]

    print(dicClothes)
    for key in dicClothes.keys():
        answer = answer * (len(dicClothes[key])+1)

    answer = answer - 1
    return answer

a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution = solution(a)
print(solution)