s = int(input())

cnt = 0
ans = 0
for i in range(1, s+1):
    cnt += i
    if cnt >= s:
        ans = i
        break

print(ans if cnt == s else ans-1)