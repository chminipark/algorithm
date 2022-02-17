import sys

input = sys.stdin.readline

t = int(input())
t_list = [int(input()) for _ in range(t)]
bin_list = []

for i in t_list:
    bin_list.append(str(bin(i))[2:])

for i in bin_list:
    length = len(i)
    for j in reversed(range(length)):
        if i[j] == '1':
            print(length-j-1, end=' ')
    print()