def check(stones, mid, k):
    possible = k

    for s in stones:
        if s - mid <= 0:
            possible -= 1
            if possible == 0:
                return False
        else:
            possible = k
    return True

def solution(stones, k):
    left, right = min(stones), max(stones)

    ans = 0
    while left <= right:
        mid = (left + right) // 2

        if check(stones, mid, k):
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    
    return ans




    






'''
[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	3	3

'''