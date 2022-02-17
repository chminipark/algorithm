def solution(n, edge):
    from collections import deque

    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    visited = [0] * (n+1)
    visited[1] = 1

    max_dist = 0
    while q:
        cur = q.popleft()

        for nex in graph[cur]:
            if visited[nex] == 0:
                visited[nex] = visited[cur] + 1
                max_dist = max(max_dist, visited[nex])
                q.append(nex)

    return visited.count(max_dist)

    









'''
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

'''