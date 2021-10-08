import sys

N, C = map(int, sys.stdin.readline().split())
homeList = list()

for i in range(N):
    homeList.append(int(sys.stdin.readline()))

homeList = sorted(homeList)
maxDistance = 0

def setRouter(homelist, c):
    def compareRouter(chosen):
        global maxDistance
        if c == len(chosen):
            close = chosen[1] - chosen[0]
            if c == 2:
                if maxDistance < close:
                    maxDistance = close
            else:
                for i in range(1, len(chosen)-1):
                    if close > chosen[i+1]-chosen[i]:
                        close = chosen[i+1]-chosen[i]
                if maxDistance < close:
                    maxDistance = close
            return True
        else:
            return False

    combi = []
    nxt = 0
    delete = 0
    while True:
        combi.append(homelist[nxt])
        if compareRouter(combi):
            if combi == homelist[len(homelist)-c:]:
                return
            for i in range(1,c+1):
                if combi[len(combi)-i] == homelist[len(homelist)-i]:
                    delete += 1
                else:
                    break
            if delete > 0:
                combi = combi[:len(combi)-delete]
                delete = 0
            nxt = homelist.index(combi[-1])+1
            combi.pop()
        else:
            nxt = homelist.index(combi[-1])+1

setRouter(homeList, C)

print(maxDistance)


#https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations