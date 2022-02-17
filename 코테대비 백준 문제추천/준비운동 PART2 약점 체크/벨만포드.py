import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# graph = [[] for _ in range(m+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a,b,c))

inf = sys.maxsize
memo = [inf] * (n+1)
memo[1] = 0

def bel():
    for i in range(n):
        for j in range(m):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            cur_wei = graph[j][2]
            next_wei = memo[cur_node] + cur_wei

            if memo[cur_node] != inf and next_wei < memo[next_node]:
                memo[next_node] = next_wei

                if i == n-1:
                    return False
    else:
        return True

if bel():
    for i in range(2, n+1):
        print(-1 if memo[i] == inf else memo[i])
else:
    print(-1)
