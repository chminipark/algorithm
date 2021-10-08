import sys
input = sys.stdin.readline

n = int(input())
s = []
sol = [0]*n

for _ in range(n):
    s.append(int(input()))

if n == 1:
    print(s[0])
elif n == 2:
    print(s[0]+s[1])
elif n == 3:
    print(max(s[2] + s[1], s[2] + s[0]))
else:
    sol[0] = s[0]
    sol[1] = s[0] + s[1]
    sol[2] = max(s[2] + s[1], s[2] + s[0])

    for i in range(3, n):
        sol[i] = max(sol[i-3]+s[i-1]+s[i], sol[i-2]+s[i])

    print(sol[-1])