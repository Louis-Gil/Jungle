# 수정 필요
import sys
input = sys.stdin.readline

num = int(input())
graph = []
for i in range(num):
    graph.append(list(map(int,input().split())))

dp = [[-1]*num for _ in range(num)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(sy, sx, count):
    if dp[sy][sx] != -1:
        return dp[sy][sx]

    ways =0
    for i in range(4):
        ay = sy + dy[i]
        ax = sx + dx[i]

                
        if 0<= ax < num and 0<= ay < num and graph[sy][sx]<graph[ay][ax]:
            temp = dfs(ay, ax, count+1)
            if ways < temp:
                ways = temp

    dp[sy][sx] = count
    return dp[sy][sx]


for i in range(num):
    for j in range(num):
        if dp[i][j] == -1:
            dfs(i,j,0)
print(dp)