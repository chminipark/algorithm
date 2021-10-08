import itertools
import collections

def solution(orders, course):
    answer = []
    for c in course:
        candidates = []
        for order in orders:
            for i in itertools.combinations(order, c):
                combi = ''.join(sorted(i))
                candidates.append(combi)
        
        sorted_candidates = collections.Counter(candidates).most_common()

        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and sorted_candidates[0][1]]
    
    return sorted(answer)

o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
c = [2,3,4]

solution(o, c)




import itertools
import collections
def solution(orders, course):
    answer = []
    

    for c in course:
        combi_list = []
        for o in orders:
            for i in itertools.combinations(''.join(sorted(o)), c):
                combi_list.append(''.join(i))
 
        sortcounterlist = collections.Counter(combi_list)
        sortcounterlist = sortcounterlist.most_common()
        most_cnt = sortcounterlist[0][1]
        for j in sortcounterlist:
            if j[1] == most_cnt:
                answer.append(j[0])
    
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))
