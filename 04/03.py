# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N = int(sys.stdin.readline())
#     coins = list(map(int, sys.stdin.readline().split()))
#     coins.insert(0, 0)
#     M = int(sys.stdin.readline())

#     dp = [[0] * (M+1) for i in range(N+1)]
#     for i in range(N+1):
#         dp[i][0] = 1

#     for j in range(1, N+1):
#         for i in range(1, M+1):
#             dp[j][i] = dp[j-1][i]
#             if i-coins[j] >= 0:
#                 dp[j][i] += dp[j][i-coins[j]]
#     print(dp[N][M])
# 출처: https://d-cron.tistory.com/23 [D cron:티스토리]

import sys
Times = int(input())
for _ in range(Times):
    N = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(input())

    dp=[0]*(M+1)
    dp[0]=1
    for coin in coins:
        for i in range(1,M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])
