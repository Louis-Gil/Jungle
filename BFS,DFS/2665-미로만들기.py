# https://www.acmicpc.net/problem/2665
import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    heap = [(0, 0, 0)]
    visited[0][0] = 1
    while heap:
        count, y, x = heapq.heappop(heap)
        if y == N-1 and x == N-1:
            return count
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and visited[ty][tx] == 0:
                visited[ty][tx] = 1
                if graph[ty][tx] == 1:
                    heapq.heappush(heap, (count, ty, tx))
                else: heapq.heappush(heap, (count+1, ty, tx))
result = bfs()
print(result)