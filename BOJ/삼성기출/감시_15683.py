import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cctv = []
cctv.append((-1,-1))
office = []
for i in range(n):
    line = list(input().strip().split())
    office.append(line)
    if not (one and two and three and four and five):
        for j in range(m):
            if line[j] == '1':
                cctv.append((i,j))
            if line[j] == '2':
                cctv.append((i,j))
            if line[j] == '3':
                cctv.append((i,j))
            if line[j] == '4':
                cctv.append((i,j))
            if line[j] == '5':
                cctv.append((i,j))

def observe(cctv_num, cctv_co):
    if cctv_num == 1:
        ncctv_co = cctv_co
        dire = []
        max_count = 0
        for i in [[1,0],[0,1],[-1,0],[0,-1]]:
            count = 0
            while True:
                ncctv_co = (ncctv_co[0]+i[0], ncctv_co[1]+i[1])
                if 0 <= ncctv_co[0] < n and 0 <= ncctv_co[1] < m:
                    