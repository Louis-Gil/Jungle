import sys
from collections import deque

col, row, level = map(int, input().split())
graph = []
queue = deque([])

for i in range(level):
    tmp = []
    for j in range(row):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(col):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    graph.append(tmp)
print(col, row, level, graph)

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    z, y, x = queue.popleft()

    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0 <= c < level and 0 <= b < row and 0 <= a < col and graph[c][b][a]==0:
            queue.append([c,b,a])
            graph[c][b][a] = graph[z][y][x]+1

day = 0

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)