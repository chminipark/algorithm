import sys
input = sys.stdin.readline

N = int(input())
p = []

for _ in range(N):
    p.append(list(map(int, input().split())))

one = 0
zero = 0

def devide(n):
    global one, zero
    for i in n:
        if not all(i): break
    else:
        one += 1
        return
    for i in n:
        if any(i): break
    else:
        zero += 1
        return

    half = len(n)//2

    devide(slicing(n, 0, 0, half))
    devide(slicing(n, 0, half, half))
    devide(slicing(n, half, 0, half))
    devide(slicing(n, half, half, half))

def slicing(n, i, j, half):
    sliced = []
    for y in range(j, j+half):
        sliced.append(n[y][i:i+half])
    return sliced

devide(p)
print(zero)
print(one)