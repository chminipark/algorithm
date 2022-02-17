def solution(money):
    dp1 = [0] * (len(money))
    dp2 = [0] * (len(money))

    # 1
    dp1[0] = money[0]
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])

    # 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
    
    return max(dp1[-2], dp2[-1])






'''
[1, 2, 3, 1]	4

dp[i] = max(dp[i-2] + money[i], dp[i-1])

'''