import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

num = int(input())
graph = []
for i in range(num):
    graph.append(list(map(int,input().split())))
dp = [[-1]*num for _ in range(num)]

def dfs(sy, sx):
    if sx == num-1 and sy == num-1:
        return 1
    if dp[sy][sx] != -1:
        return dp[sy][sx]

    ways =0
    dy = [graph[sy][sx], 0]
    dx = [0, graph[sy][sx]]
    for i in range(2):
        ay = sy + dy[i]
        ax = sx + dx[i]

        if ax < num and ay < num:
            if graph[ay][ax]==0 and sx != num-1 and sy != num-1:
                continue
            ways += dfs(ay, ax)

    dp[sy][sx] = ways
    return dp[sy][sx]
print(dfs(0,0))