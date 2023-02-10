# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]
visited = [[0] * col for _ in range(row)]

queue = deque([])

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(Dy, Dx):
    while queue:
        y, x = queue.popleft()
        if graph[Dy][Dx] == 'S':
            return visited[Dy][Dx]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < col and 0 <= ny < row:
                if (graph[ny][nx] == '.' or graph[ny][nx] == 'D') and graph[y][x] == 'S':
                    graph[ny][nx] = 'S'
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                elif (graph[ny][nx] == '.' or graph[ny][nx] == 'S') and graph[y][x] == '*':
                    graph[ny][nx] = '*'
                    queue.append((ny, nx))
    return 'KAKTUS'
        
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'S':
            queue.append((i,j))
        elif graph[i][j] == 'D':
            Dy, Dx = i, j

for i in range(row):
    for j in range(col):
        if graph[i][j] == '*':
            queue.append((i,j))
            
print(bfs(Dy, Dx))