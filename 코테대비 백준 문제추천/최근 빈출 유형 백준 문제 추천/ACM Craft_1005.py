import collections
import sys

def solution(n, w, build_time, graph, indegree):
    dp = [0] * (n+1)
    q = collections.deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = build_time[i]
    
    while q:
        cur = q.popleft()

        for nex in graph[cur]:
            dp[nex] = max(dp[nex], dp[cur] + build_time[nex])
            indegree[nex] -= 1
            if indegree[nex] == 0:
                q.append(nex)
    
    return dp[w]


if __name__ == '__main__':
    input = sys.stdin.readline
    ans = []
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        build_time = [-1] + list(map(int, input().split()))
        graph = [[] for _ in range(n+1)]
        indegree = [0] * (n+1)
        for _ in range(k):
            a, b = map(int, input().split())
            graph[a].append(b)
            indegree[b] += 1
        w = int(input())
        ans.append(solution(n, w, build_time, graph, indegree))
    print(*ans, sep='\n')
    