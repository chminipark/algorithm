import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, r, q = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
query = [int(input()) for _ in range(q)]
count = [0] * (n+1)

def makeCount(x):
    count[x] = 1

    for i in edges[x]:
        if not count[i]:
            makeCount(i)
            count[x] += count[i]

makeCount(r)

for i in query:
    print(count[i])