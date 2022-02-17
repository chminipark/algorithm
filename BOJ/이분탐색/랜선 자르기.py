import sys

def possible_Cnt(cnt, l_list):
    ans = 0
    for l in l_list:
        ans += l // cnt
    return ans

def bin(need, l_list):
    l_list.sort()
    start, end = 1, l_list[-1]

    ans = 0
    while start <= end:
        mid = (start+end) // 2

        if possible_Cnt(mid, l_list) >= need:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    k, n = map(int, input().split())
    l_list = [int(input()) for _ in range(k)]
    print(bin(n, l_list))
