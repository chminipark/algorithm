a, b = map(int, input().split())
memo = [0] * b

def solution():
    idx = 0
    cnt = 1
    while True:
        for i in range(cnt):
            memo[idx] = cnt
            idx += 1
            if idx == b:
                return
        cnt += 1

solution()

print(sum(memo[a-1:b]))