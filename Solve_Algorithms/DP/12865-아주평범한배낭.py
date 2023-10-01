# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

stuff_num, weight_limit = map(int, input().split())
arr = [[0,0]]
for _ in range(stuff_num):
    arr.append(list(map(int, input().split())))
arr.sort()

dp = [[0] * (weight_limit+1) for _ in range(stuff_num+1)]

for i in range(1, stuff_num+1):
    weight, value = arr[i][0], arr[i][1]
    for j in range(1, weight_limit+1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
print(dp[-1][-1])