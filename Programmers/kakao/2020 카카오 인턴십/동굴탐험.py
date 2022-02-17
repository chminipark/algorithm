def solution(n, path, order):
    before = dict()
    after = dict()
    graph = [[] for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in order:
        if b == 0:
            return False
        before[b] = a
    
    visited = [False] * (n)
    cnt_visited = 0
    stack = [0]
    while stack:
        cur_node = stack.pop()

        if cur_node in before and not visited[before[cur_node]]:
            after[before[cur_node]] = cur_node
            continue
        
        visited[cur_node] = True
        cnt_visited += 1
        for nex_node in graph[cur_node]:
            if not visited[nex_node]:
                stack.append(nex_node)

        if cur_node in after:
            stack.append(after[cur_node])
    
    return cnt_visited == n







'''
[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]	[[4,1],[5,2]]	true



위상, visited

'''