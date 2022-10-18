import sys
input = sys.stdin.readline

number = int(input())
list_figure = list(map(int, input().split()))
dp = [1] * number

for i in range(1, number):
    for j in range(i):
        if list_figure[i] > list_figure[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
