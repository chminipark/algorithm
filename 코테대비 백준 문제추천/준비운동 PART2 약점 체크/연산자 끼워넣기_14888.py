# import sys

# input = sys.stdin.readline

# n = int(input())
# # n_list = list(map(int, input().split()))
# n_list = list(input().split())
# cal = list(map(int, input().split()))
# c = ['+', '-', '*', '//']
# cal_list = []
# for i in range(4):
#     cal_list += [c[i]] * cal[i]

# sum_cal = len(cal_list)

# mx = -sys.maxsize
# mn = sys.maxsize

# s = []
# def back(result, idx):
#     global mx, mn
#     if idx == sum_cal:
#         mx = max(result, mx)
#         mn = min(result, mn)
#         return

#     for i in range(sum_cal):
#         temp = result
#         if i in s:
#             continue
#         result = eval(str(result) + cal_list[i] + n_list[i+1])
#         # print(s)
#         # print(i)
#         # print(str(result) + cal_list[i] + n_list[i])
#         # print(a)
#         s.append(i)
#         back(result, idx+1)
#         s.pop()
#         result = temp


# back(int(n_list[0]), 0)
# print(mx)
# print(mn)






# n = 3
# s = []
# def back():
#     if len(s) == n:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(n):
#         if i in s:
#             continue
#         s.append(i)
#         back()
#         s.pop()

# back()

################## ㄸㄸ다시시ㅣㅅ푸루푸풀기기기기기



import sys

input = sys.stdin.readline

n = int(input())
n_list = list(input().split())
c = list(map(int, input().split()))
cc = ['+', '-', '*', '//']
cal = []
for i in range(4):
    cal += [cc[i]] * c[i]

mx = -sys.maxsize
mn = sys.maxsize

sum_cal = len(cal)

s = []
def back(result, idx):
    global mx, mn

    if idx == n-1:
        mx = max(mx, result)
        mn = min(mn, result)
        return

    for i in range(sum_cal):
        if i in s:
            continue
        s.append(i)
        a = eval(str(result) + cal[i] + n_list[len(s)])
        if result < 0 and int(n_list[len(s)]) > 0 and cal[i] == '//':
            a = eval(str(abs(result)) + cal[i] + n_list[len(s)]) * (-1)
        back(a, idx+1)
        s.pop()

back(int(n_list[0]), 0)
print(mx)
print(mn)