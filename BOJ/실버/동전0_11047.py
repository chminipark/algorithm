import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []

for _ in range(N):
    coin.append(int(input()))

coin = reversed(coin)
cnt = 0

while K:
    for i in coin:
        if K//i >= 1:
            cnt += K//i
            K -= i*(K//i)

print(cnt)
        