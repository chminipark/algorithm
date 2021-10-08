import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
iscontain_list = list(map(int, input().split()))

a_list.sort()

def bianrysearch(i: int, l: list):
    left = 0
    right = len(a_list)-1
    while left <= right:
        middle = (left+right)//2
        if i == l[middle]:
            return 1
        elif l[middle] < i:
            left = middle+1
        else:
            right = middle-1
    return 0

for i in iscontain_list:
    print(bianrysearch(i, a_list))
