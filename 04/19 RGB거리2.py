import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def minPaint(selHouse):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = arr[0]
    
    for i in range(3):
        if i == selHouse:
            dp[1][i] = 1e9
            continue
        dp[1][i] = arr[1][i] + arr[0][selHouse]

    for i in range(2, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    dp[n - 1].pop(selHouse)
    return min(dp[n - 1])

ans = 1e9
for i in range(3):
    ans = min(ans, minPaint(i))

print(ans)