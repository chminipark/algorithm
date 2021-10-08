import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def postorder(start, end):

    if start > end:
        return

    right_start = end+1
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            right_start = i
            break

    #left
    postorder(start+1, right_start-1)
    #right
    postorder(right_start, end)
    #parent
    print(pre[start])

pre = []
count = 0
while True:
    try:
        temp = int(input())
    except:
        break
    pre.append(temp)

postorder(0, len(pre)-1)





# def solution(start, end):
#     if start > end:
#         return

#     div = end + 1

#     for i in range(start + 1, end + 1):
#         # 루트 보다 큰 지점 --> 오른쪽 서브 트리
#         if tree[start] < tree[i]:
#             div = i
#             break

#     solution(start + 1, div - 1)
#     solution(div, end)
#     print(tree[start])


# import sys
# sys.setrecursionlimit(10 ** 9)

# tree = []
# count = 0
# while count <= 10000:

#     try:
#         temp = int(input())
#     except:
#         break
#     tree.append(temp)
#     count += 1

# solution(0, len(tree) - 1)