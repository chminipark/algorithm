import sys
input = sys.stdin.readline

N = int(input())
v = []

for _ in range(N):
    v.append(input().strip())

def compress(a):
    check = a[0][0]
    ischeck = True
    for i in a:
        for j in i:
            if j != check:
                ischeck = False
                break
        if not ischeck:
            break
    
    if ischeck:
        return check
    elif len(a) == 2:
        result = ''
        for i in a:
            result += i
        return '('+result+')'
    else:
        half = len(a)//2
        return f'({compress(slicing(a, 0, 0, half))}{compress(slicing(a, half, 0, half))}{compress(slicing(a, 0, half, half))}{compress(slicing(a, half, half, half))})'
    
def slicing(n, i, j, half):
    sliced = []
    for y in range(j, j+half):
        sliced.append(n[y][i:i+half])
    return sliced

print(compress(v))

