def makeTable(s):
    pattern = [0] * len(s)

    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j > 0:
            j = pattern[j-1]
        if s[i] == s[j]:
            j += 1
            pattern[i] = j 
    
    return pattern

def check(s):
    # len(s) // (len(s) - pattern[-1]
    table = makeTable(s)

    if len(s) % (len(s) - table[-1]) != 0:
        return 1
    else:
        return len(s) // (len(s) - table[-1])

ans = []
while True:
    t = input()
    if t == '.':
        break
    ans.append(check(t))

print(*ans, sep='\n')