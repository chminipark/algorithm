### BFS ###
import collections

n = int(input())
q = collections.deque()
visited = [0] * (n+1)
q.append((n, 0))
# (cur_num, cur_cnt)

cnt = 0
while q:
    cur_num, cur_cnt = q.popleft()
    cnt += 1
    if cur_num == 1:
        print(cur_cnt)
        break

    if cur_num % 3 == 0 and visited[cur_num//3] == 0:
        visited[cur_num//3] = cur_num
        q.append((cur_num//3, cur_cnt+1))
    
    if cur_num % 2 == 0 and visited[cur_num//2] == 0:
        visited[cur_num//2] = cur_num
        q.append((cur_num//2, cur_cnt+1))
    
    if visited[cur_num-1] == 0:
        visited[cur_num-1] = cur_num
        q.append((cur_num-1, cur_cnt+1))

print(cnt)
ans = [1]
idx = 1
while True:
    ans.append(visited[idx])
    if visited[idx] == n:
        break
    idx = visited[idx]

for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=' ')





### DP ###

# n = int(input())
# dist = [0] * (n+1)
# path = [0] * (n+1)

# # dist[i] = min(dist[i-1], dist[i//2], dist[i//3]) + 1
# cnt = 0
# for i in range(2, n+1):
#     cnt += 1
#     dist[i] = dist[i-1] + 1
#     path[i] = i-1

#     if i % 2 == 0 and dist[i] > dist[i//2] + 1:
#         dist[i] = dist[i//2] + 1
#         path[i] = i//2
    
#     if i % 3 == 0 and dist[i] > dist[i//3] + 1:
#         dist[i] = dist[i//3] + 1
#         path[i] = i//3
    
# print(cnt)
# print(dist[n])
# idx = n
# while True:
#     print(idx, end= ' ')
#     if idx == 1:
#         break
#     idx = path[idx]