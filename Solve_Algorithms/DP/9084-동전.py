# https://www.acmicpc.net/problem/9084
import sys

input = sys.stdin.readline

Times = int(input())
for _ in range(Times):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M+1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])
