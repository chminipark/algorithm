# import sys

# input = sys.stdin.readline

# s = input().strip()
# p = input().strip()
# table = [0] * (len(s))

# def makeTable():
#     j = 0
#     for i in range(1, len(s)):
#         while j > 0 and s[i] != s[j]:
#             j = table[j-1]
#         if s[i] == s[j]:
#             j += 1
#             table[i] = j

# def kmp():
#     makeTable()
#     j = 0
#     for i in range(len(s)):
#         while j > 0 and s[i] != p[j]:
#             j = table[j-1]
#         if s[i] == p[j]:
#             if j == len(p)-1:
#                 return True
#             else:
#                 j += 1
#     else:
#         return False

# print(1 if kmp() else 0)


import sys

input = sys.stdin.readline

s = input().strip()
p = input().strip()
pattern = [0] * (len(s))

def makePattern():
    j = 0
    for i in range(1, len(p)):
        while p[i] != p[j] and j > 0:
            j = pattern[j-1]
        if p[i] == p[j]:
            j += 1
            pattern[i] = j

def kmp():
    makePattern()
    j = 0
    for i in range(len(s)):
        while s[i] != p[j] and j > 0:
            j = pattern[j-1]
        if s[i] == p[j]:
            if j == len(p)-1:
                return True
            else:
                j += 1
    else:
        return False

print(1 if kmp() else 0)