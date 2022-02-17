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

l = int(input())
word = input().strip()
print(len(word) - makeTable(word)[-1])