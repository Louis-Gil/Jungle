import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    coins.insert(0, 0)
    M = int(sys.stdin.readline())

    dp = [[0] * (M+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j]
            if j-coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    print(dp[N][M])

# import sys
# Times = int(input())
# for _ in range(Times):
#     N = int(input())
#     coins = list(map(int, sys.stdin.readline().split()))
#     M = int(input())

#     dp=[0]*(M+1)
#     dp[0]=1
#     for coin in coins:
#         for i in range(1,M+1):
#             if i >= coin:
#                 dp[i] += dp[i-coin]
#     print(dp[M])
