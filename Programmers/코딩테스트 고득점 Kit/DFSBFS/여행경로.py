def solution(tickets):
    tickets_dic = dict()
    for i in tickets:
        tickets_dic[i[0]] = []
    for a, b in tickets:
        tickets_dic[a].append(b)
    for i in tickets_dic.keys():
        tickets_dic[i] = list(reversed(sorted(tickets_dic[i])))

    stack = []
    # [[path], {visited}, cnt]
    stack.append([['ICN'], tickets_dic, 0])

    answer = []
    while stack:
        print(stack)
        path, visited, cnt = stack.pop()
        path_cur = path[-1]

        for _ in range(len(visited[path_cur])):
            tmp_visited = visited.copy()
            tmp_path = path[:]
            
            nex = tmp_visited[path_cur].pop()
            tmp_path.append(nex)

            if cnt + 1 == len(tickets):
                print(tmp_path)
            else:
                stack.append([tmp_path, tmp_visited, cnt+1])




solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])

'''
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
dfs
가지치기
not in visited
'''






from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer