# https://www.acmicpc.net/problem/2748

N = int(input())

def dp(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    dp = [[] for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 1
    temp = 1
    while temp < N:
        temp += 1
        dp[temp] = dp[temp-1] + dp[temp-2]
    return dp[N]
print(dp(N))