import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w_list = [input().strip() for _ in range(n)]

if k < 5:
    print(0)
    sys.exit()

check = {'a', 'n', 't', 'i', 'c'}
possible = k - 5
ans = 0
for word in w_list:
    new = set(word) - check
    isnew = set(word) - check
    for i in new:
        if possible == 0:
            break
        possible -= 1
        check.add(i)
        isnew.discard(i)
    
    if not isnew:
        ans += 1

print(ans)


    # while possible > 0 and new:

# a = {1,2,3}
    # for _ in range(possible):
    #     if new:
    #         check.add(new[0])