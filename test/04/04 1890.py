import sys
input = sys.stdin.readline

N = int(input())

board = [ list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(1,10):
            if i-k >=0 and k == board[i-k][j]:
                dp[i][j] += dp[i-k][j] 

            if j-k >=0 and k == board[i][j-k]:
                dp[i][j] += dp[i][j-k] 

print(dp[N-1][N-1])