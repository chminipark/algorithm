import sys

input = sys.stdin.readline
train = []

for _ in range(10):
    a, b = map(int,input().split())
    train.append((a,b))

cp = 0
mx = 0
for x,y in train:
    cp = (cp-x)+y
    mx = max(cp, mx)

print(mx)