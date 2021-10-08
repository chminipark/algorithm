import sys

wordList = set()

for _ in range(int(sys.stdin.readline())):
    word = str(sys.stdin.readline().rstrip())
    wordList.add((word, len(word)))

wordList = list(wordList)

wordList.sort(key = lambda x: (x[1], x[0]))

for i in wordList:
    print(i[0])