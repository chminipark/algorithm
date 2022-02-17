import sys
input = sys.stdin.readline

n, l = map(int, input().split())

def check(line):
    isplaced = [0 for _ in range(len(line))]
    for i in range(len(line)-1):
        # 1
        if abs(line[i+1] - line[i]) >= 2:
            return False
        if abs(line[i+1] - line[i]) == 1:
            if line[i+1] > line[i]:
                if not (0 <= i-(l-1)):
                    return False
                else:
                    for j in range(i-(l-1), i+1):
                        if isplaced[j] == 1 or line[j] != line[i]:
                            return False
                        else:
                            isplaced[j] = 1
            else:
                if not (i+1+(l-1) < n):
                    return False
                else:
                    for j in range(i+1, i+1+(l-1)+1):
                        if isplaced[j] == 1 or line[j] != line[i+1]:
                            return False
                        else:
                            isplaced[j] = 1
    else:
        return True

answer = 0
mapp = []
for _ in range(n):
    line = list(map(int, input().split()))
    mapp.append(line)
    if check(line):
        answer += 1

for i in range(n):
    line = []
    for j in range(n):
        line.append(mapp[j][i])
    if check(line):
        answer += 1

print(answer)