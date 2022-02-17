def solution(n, times):
    left, right = 1, max(times) * n

    ans = 0
    while left <= right:
        mid = (left+right) // 2

        tmp = n
        for i in times:
            tmp -= mid//i

            if tmp <= 0:
                ans = mid
                right = mid-1
                break
        
        if tmp > 0:
            left = mid + 1
    
    return ans