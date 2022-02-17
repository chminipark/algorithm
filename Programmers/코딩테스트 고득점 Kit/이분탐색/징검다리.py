def solution(distance, rocks, n):
    left, right = 0, distance
    rocks.sort()
    rocks.append(distance)

    ans = 0
    while left <= right:
        mid = (left + right) // 2

        remove_cnt = 0
        current = 0
        min_diff = float('inf')

        for i in range(len(rocks)):
            diff = rocks[i] - current

            if diff < mid:
                remove_cnt += 1
            else:
                current = rocks[i]
                min_diff = min(min_diff, diff)
        
        if remove_cnt > n:
            right = mid - 1 
        else:
            left = mid + 1
            ans = min_diff
    
    return ans