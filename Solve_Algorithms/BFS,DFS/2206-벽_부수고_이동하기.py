# https://www.acmicpc.net/problem/2206
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dist = []

for i in range(N):
    dist.append(list(map(int, sys.stdin.readline().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs(x, y, z):
    que = deque()
    que.append((x, y, z))
    
    while que:
        a, b, c = que.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if dist[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                que.append((nx, ny, 1))
            elif dist[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                que.append((nx, ny, c))
    return -1

print(bfs(0,0,0))
