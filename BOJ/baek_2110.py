import sys

N, C = map(int, sys.stdin.readline().split())
homeList = list()

for i in range(N):
    homeList.append(int(sys.stdin.readline()))

homeList = sorted(homeList)
maxDistance = 0

def setRouter(homelist, c):
    def generate(chosen):
        global maxDistance
        
        if c == len(chosen):
            close = chosen[1] - chosen[0]
            if c == 2:
                if maxDistance < close:
                    maxDistance = close
                return
            else:
                for i in range(1, len(chosen)-1):
                    if close > chosen[i+1]-chosen[i]:
                        close = chosen[i+1]-chosen[i]
                if maxDistance < close:
                    maxDistance = close
                return

        start = homelist.index(chosen[-1])+1 if chosen else 0
        for i in range(start, len(homelist)):
            chosen.append(homelist[i])
            generate(chosen)
            chosen.pop()
    generate([])

setRouter(homeList, C)

print(maxDistance)


#https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations