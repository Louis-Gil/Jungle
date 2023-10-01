# https://www.acmicpc.net/problem/1303
import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int, input().split())

dp = [list(input()) for _ in range(row)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

white_power = 0
blue_power = 0

def bfs (r, c, color):
    cnt = 1
    q = deque()
    q.append((r, c))
    dp[r][c] = 0
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            
            if 0 <= nr < row and 0 <= nc < col :
                if dp[nr][nc] == color:
                    q.append((nr, nc))
                    dp[nr][nc] = 0
                    cnt += 1
    return cnt
        
        
        
    

for i in range(row):
    for j in range(col):
        if dp[i][j] == 'W':
            white_power += bfs(i, j, 'W') ** 2
        elif dp[i][j] == 'B':
            blue_power += bfs(i, j, 'B') ** 2
print(white_power, blue_power)