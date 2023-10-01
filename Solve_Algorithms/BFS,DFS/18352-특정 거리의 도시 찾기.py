# https://www.acmicpc.net/problem/18352
import sys
from collections import deque
input = sys.stdin.readline

city_num, road_num, distance, start = map(int, input().split())
graph = [[] for _ in range(city_num+1)]
for i in range(road_num):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [0] * (city_num+1)
result = []

def bfs(start, distance):
    queue = deque()
    queue.append([start, 1])
    visited[start] = 1
    while queue:
        city, dist = queue.popleft()
        if dist == distance+1:
            result.append(city)
        for i in graph[city]:
            if visited[i] == 0:
                visited[i] = dist + 1
                queue.append([i, dist+1])


bfs(start, distance)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')
