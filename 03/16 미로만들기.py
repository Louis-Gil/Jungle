import sys
import heapq
input = sys.stdin.readline

line = int(input())

graph = [[] for _ in range(line+1)]
for i in range(1, line+1):
    graph[i] = [0] + list(map(str, input().strip()))
# print(line, graph)

def BFS():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    heap = []
    visited = [[0] * (line+1) for _ in range(line+1)]
    
    heapq.heappush(heap, [0, 1, 1])
    
    while heap:
        count, y, x = heapq.heappop(heap)
        visited[y][x] = 1
        if y == line and x == line:
            print(count)
            return

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 < ty <= line and 0 < tx <= line and visited[ty][tx] == 0 :
                visited[ty][tx] = 1
                if graph[ty][tx] == '0':
                    heapq.heappush(heap, [count+1, ty, tx])
                else: heapq.heappush(heap, [count, ty, tx])




BFS()