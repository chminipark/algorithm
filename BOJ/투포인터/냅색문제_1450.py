# import sys
# input = sys.stdin.readline

# n,c = map(int,input().split())
# w = list(map(int,input().split()))
# w1,w2 = w[:n//2],w[n//2:]
# wl,wr = [],[]

# # 완전 탐색
# def bf(arr,seq,idx,summ):
#     if len(arr) == idx:
#         seq.append(summ)
#         return seq
    
#     bf(arr,seq,idx+1,summ)
#     bf(arr,seq,idx+1,summ+arr[idx])
    
#     return seq

# # 절반씩 탐색
# wl = bf(w1,wl,0,0)
# wr = sorted(bf(w2,wr,0,0))
# r = 0


# for i in wl:
#     if c-i < 0:
#         continue
    
#     # 이분 탐색
#     start,end = 0,len(wr)
#     while(start < end):
#         mid = (start+end)//2
#         if wr[mid] <= c-i:
#             start = mid+1
#         else:
#             end = mid
#     r+= start
# print(r)

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))

def bruteforce(w_list, idx, to_save, weight):
    if idx == len(w_list):
        to_save.append(weight)
        return
    
    bruteforce(w_list, idx+1, to_save, weight)
    bruteforce(w_list, idx+1, to_save, weight+w_list[idx])

wl, wr = w[:n//2], w[n//2:]
w1, w2 = [], []

bruteforce(w, 0, w1, 0)
bruteforce(w, 0, w2, 0)

w2.sort()
ans = 0

for i in w1:
    if c < i:
        continue

    start, end = 0, len(w2)
    while (start < end):
        mid = (start+end)//2
        if c-i >= w2[mid]:
            start = mid+1
        else:
            end = mid
    ans += start

print(ans)