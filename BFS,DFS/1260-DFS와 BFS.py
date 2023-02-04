# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline
point_num, line_num, start_num = map(int, input().split())

graph = [[0] * (point_num+1) for _ in range(point_num+1)]
visited1 = [0] * (point_num + 1)
visited2 = [0] * (point_num + 1)

for i in range(line_num):
    point1, point2 = map(int, input().split())
    graph[point1][point2] = graph[point2][point1] = 1
print(graph)

def dfs(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(1, point_num+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, point_num+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1

dfs(start_num)
print()
bfs(start_num)
print()