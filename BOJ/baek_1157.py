import sys

word = str(sys.stdin.readline().rstrip())
word = word.upper()
already = set()
count = 0
resultCount = 0
result = "?"

if len(word) == 1:
    result = word
else:
    for i in range(len(word)-1):
        if word[i] in already:
            continue
        for j in range(i+1,len(word)):
            if word[j] in already:
                continue
            if word[i] == word[j]:
                count += 1
        if count == resultCount:
            result = "?"
        elif count > resultCount:
            resultCount = count
            result = word[i]
        count = 0
        already.add(word[i])

print(result)

#rstrip()