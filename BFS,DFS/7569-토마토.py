# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
input = sys.stdin.readline

col, row, level = map(int, input().split())
graph = []
visited = [[[0] * col for _ in range(row)] for _ in range(level)]
queue = deque([])

for i in range(level):
    level_temp = []
    for j in range (row):
        level_temp.append(list(map(int, input().split())))
        for k in range(col):
            if level_temp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(level_temp)
    
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dl = [0, 0, 0, 0, 1, -1]

def dfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dl[i]
            if 0 <= c < level and 0 <= b < row and 0 <= a < col and graph[c][b][a] == 0:
                queue.append([c, b, a])
                graph[c][b][a] = graph[z][y][x] + 1
    return

dfs()
result = 0
for i in range(level):
    for j in range(row):
        if 0 in graph[i][j]:
            print(-1)
            exit()
        result = max(result, max(graph[i][j]))
print(result-1)
