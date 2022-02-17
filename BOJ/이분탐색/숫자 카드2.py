import sys
import bisect

def binarySearch_Count(num, n_list):
    left = bisect.bisect_left(n_list, num)
    right = bisect.bisect_right(n_list, num)

    return right - left

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    n_list.sort()
    for i in m_list:
        print(binarySearch_Count(i, n_list), end=' ')