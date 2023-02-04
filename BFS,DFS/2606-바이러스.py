# https://www.acmicpc.net/problem/2606
import sys
from collections import deque

input = sys.stdin.readline
cpt = int(input())
line = int(input())
graph = [[0] * (cpt + 1) for _ in range(cpt + 1)]
visited1 = [0] * (cpt + 1)
visited2 = [0] * (cpt + 1)

for i in range(1, line+1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

count = 1
def dfs(v):
    global count
    visited1[v] = 1
    for i in range(1, cpt+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            count += 1
            dfs(i)

dfs(1)
print(count-1)

# def bfs(v):
#     q = deque()
#     q.append(v)
#     count = 0
#     while q:
#         v = q.popleft()
#         for i in range(1, cpt+1):
#             if visited2[i] == 0 and graph[v][i] == 1:
#                 q.append(i)
#                 visited2[i] = 1
#                 count += 1
#     return count

# print(bfs(1)-1)
