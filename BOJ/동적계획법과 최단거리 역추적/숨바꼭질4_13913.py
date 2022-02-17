import collections

n, k = map(int, input().split())
q = collections.deque()
dist = [0] * (100001)
path = [0] * (100001)
q.append(n)

while q:
    now = q.popleft()

    if now == k:
        break

    for i in [now+1, now-1, now*2]:
        if 0 <= i < 100001 and dist[i] == 0:
            q.append(i)
            dist[i] = dist[now] + 1
            path[i] = now

print(dist[k])
ans = ' ' + str(k)
idx = k
for _ in range(dist[k]):
    ans = ' ' + str(path[idx]) + ans
    idx = path[idx]

print(ans.strip())