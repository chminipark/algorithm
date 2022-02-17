import sys

input = sys.stdin.readline

n = int(input())

if n >= 1023:
    print(-1)
    sys.exit()    

ans = [i for i in range(10)]
s_idx = 0
idx = len(ans)
for _ in range(9):
    s_idx = len(ans) - idx
    idx = 0
    for i in range(s_idx, len(ans)):
        for p_num in range(int(str(ans[i])[0])+1, 10):
            add_num = str(p_num) + str(ans[i]) 
            idx += 1
            ans.append(int(add_num))

ans.sort()
print(ans[n])
        
            






'''

9876543210

'''