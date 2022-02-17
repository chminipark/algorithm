import sys
import collections

def solution(graph, indegree, m):
    strahler = [(1,0)] * (m+1)
    # (max_i, cnt)

    q = collections.deque()
    for i in range(1,m+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur_node = q.popleft()

        if cur_node == m:
            return strahler[cur_node][0]

        for i in graph[cur_node]:
            if strahler[i][0] < strahler[cur_node][0]:
                strahler[i] = (strahler[cur_node][0], 1)
            elif strahler[i][0] == strahler[cur_node][0]:
                strahler[i] = (strahler[i][0], strahler[i][1]+1)

            indegree[i] -= 1
            if indegree[i] == 0:
                if strahler[i][1] >= 2:
                    strahler[i] = (strahler[i][0]+1, 0)
                q.append(i) 


if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())
    ans = []
    for _ in range(t):
        k, m, p = map(int, input().split())
        graph = [[] for _ in range(m+1)]
        indegree = [0] * (m+1)
        for _ in range(p):
            a, b = map(int, input().split())
            graph[a].append(b)
            indegree[b] += 1
        ans.append((k, solution(graph, indegree, m)))
    for case in ans:
        print(*case)
        