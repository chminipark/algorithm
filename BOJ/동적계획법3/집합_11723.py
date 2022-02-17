import sys

input = sys.stdin.readline

m = int(input())
# s = 0

for _ in range(m):
    cmd = input().strip().split()

    if cmd[0] == 'add':
        s = s | (1 << cmd[-1])
    elif cmd[0] == 'remove':
        s = s & ~(1 << cmd[-1])
    elif cmd[0] == 'check':
        if s & (1 << cmd[-1]) == 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'toggle':
        s = s ^ (1 << cmd[-1])
    elif cmd[0] == 'all':
        s = (1 << 20) - 1
    elif cmd[0] == 'empty':
        s = 0

s = 0
s = s | (1 << 1)
print()


'''
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
'''