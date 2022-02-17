def makeTable(a):
    pattern = [0] * len(a)

    j = 0
    for i in range(1, len(a)):
        while a[i] != a[j] and j > 0:
            j = pattern[j-1]
        if a[i] == a[j]:
            j += 1
            pattern[i] = j
    
    return pattern

def kmp(s, f, pattern):
    j = 0
    for i in range(len(s)):
        while s[i] != f[j] and j > 0:
            j = pattern[j-1]
        if s[i] == f[j]:
            if j == len(f) - 1:
                ans.append(i-(len(f)-1)+1)
                j = pattern[j]
            else:
                j += 1


t = input()
p = input()

ans = []
kmp(t, p, makeTable(p))
print(len(ans))
print(*ans)