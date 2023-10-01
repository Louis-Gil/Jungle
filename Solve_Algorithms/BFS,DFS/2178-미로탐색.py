# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 99999999

# def dfs(row, col, cnt):
#     global N, M, result
#     if row == N-1 and col == M-1:
#         if result > cnt:
#             result = cnt
#         return
#     for i in range(4):
#         ny = row + dy[i]
#         nx = col + dx[i]
#         if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1 and not visited[ny][nx]:
#             visited[ny][nx] = True
#             dfs(ny, nx, cnt+1)
#             visited[ny][nx] = False
            
def bfs(row, col):
    global N, M, result
    queue = deque([[row, col]])
    while queue:
        value = queue.popleft()
        for i in range(4):
            y = value[0] + dy[i]
            x = value[1] + dx[i]
            if 0 <= y < N and 0 <= x < M and graph[y][x] == 1:
                queue.append([y, x])
                graph[y][x] = graph[value[0]][value[1]] + 1
    

# visited[0][0] = True
bfs(0, 0)
print(graph[N-1][M-1])