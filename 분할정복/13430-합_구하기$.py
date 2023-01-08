# https://www.acmicpc.net/problem/13430
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = {}
def solve(n, m):
    if n == 0:
        return m % 1000000007

    if (f"{n}/{m}" in dp):
        return dp[f"{n}/{m}"]
    temp = 0
    for i in range(1,m+1):
        temp += solve(n-1, i)
    temp = temp % 1000000007
    dp[f"{n}/{m}"] = temp
    return temp
    
    
result = solve(n, m)
print(result)