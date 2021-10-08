# import sys

# _input = sys.stdin.readline

# T = int(_input())
# N = []

# for _ in range(T):
#     N.append(int(_input()))


# def fibo(n: int):
#     # n => n-1 n-2
#     n_list = []
#     n_list.append(n)
#     loop_check = True

#     while loop_check:
#         temp = []
#         for i in range(len(n_list)):
#             if n_list[i] == 0 or n_list[i] == 1:
#                 temp += n_list[i:]
#                 break
#             temp.append(n_list[i]-1)
#             temp.append(n_list[i]-2)

#         n_list = temp

#         for i in n_list:
#             if i > 1:
#                 break
#         else:
#             loop_check = False

#     return (n_list.count(0), n_list.count(1))

# for i in N:
#     ans = fibo(i)
#     print(ans[0], ans[1])

# 배열로 하나씩 줄여가며 계산했는데 바로 시간초과...

# 구글링 풀이는 미리 40까지 모두 계산한다음 계산된 배열에서 한번에 값을 찾아오는거.

import sys

input = sys.stdin.readline

T = int(input())

cnt0 = [1, 0]
cnt1 = [0, 1]

for i in range(2, 41):
    cnt0.append(cnt0[i-2] + cnt0[i-1])
    cnt1.append(cnt1[i-2] + cnt1[i-1])

for _ in range(T):
    N = int(input())
    print(cnt0[N], cnt1[N])



