import sys
sys.setrecursionlimit(10**9)

def binarySearch_recur(target, start, end, data):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return mid
    elif target < data[mid]:
        end = mid - 1
    else:
        start = mid + 1

    return binarySearch_recur(target, start, end, data)



def binarySearch(target, data):
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    n_list = list(map(int, input().split()))
    q = int(input())
    q_list = list(map(int, input().split()))

    n_list.sort()
    for i in q_list:
        print(1 if binarySearch_recur(i, 0, len(n_list)-1, n_list) != None else 0)
        # print(1 if binarySearch(i, n_list) != None else 0)

