import collections
import sys
input = sys.stdin.readline


t_list = []
t_list.append(collections.deque())
for _ in range(4):
    t_list.append(collections.deque(list(map(int, list(input().strip())))))

k = int(input())
k_list = []
for _ in range(k):
    number, direction = map(int, input().split())
    k_list.append((number, direction))

def rotate(n, d):
    count = 1
    rotate_list = []
    rotate_list.append((n,d))
    minus_n = n
    plus_n = n
    while True:
        minus_n -= 1
        if 1 <= minus_n <= 3:
            if t_list[minus_n][2] != t_list[minus_n+1][6]:
                num = minus_n
                dire = list(filter(lambda x: x[0] == (minus_n+1), rotate_list))[0][1] * (-1)
                rotate_list.append((num, dire))
            else:
                break
        else:
            break
    while True:
        plus_n += 1
        if 2 <= plus_n <= 4:
            if t_list[plus_n-1][2] != t_list[plus_n][6]:
                num = plus_n
                dire = list(filter(lambda x: x[0] == (plus_n-1), rotate_list))[0][1] * (-1)
                rotate_list.append((num, dire))
            else:
                break
        else:
            break

    for i in rotate_list:
        t_list[i[0]].rotate(i[1])

for i in k_list:
    rotate(i[0], i[1])

ans = 0
if t_list[1][0] == 1:
    ans += 1
if t_list[2][0] == 1:
    ans += 2
if t_list[3][0] == 1:
    ans += 4
if t_list[4][0] == 1:
    ans += 8

print(ans)