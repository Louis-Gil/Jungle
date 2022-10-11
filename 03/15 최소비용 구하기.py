import sys
import heapq
input = sys.stdin.readline

# 도시의 개수 N, 버스의 개수 M, 
# 출발 도시, 도착 도시, 비용
N = int(input())
M = int(input())
M_lst = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, E = list(map(int, input().split()))
    M_lst[A].append([B, E])
start, end = map(int, input().split())
visited = [1e9] * (N + 1)

# print(N, M, M_lst, start, end)

def BFS():
    heap = []
    heapq.heappush(heap, [start, 0])
    visited[start] = 0

    while heap :
        x, y = heapq.heappop(heap)
        if visited[x] < y:
            continue
        for i, j in M_lst[x]:
            target = j + y
            if target < visited[i]:
                visited[i] = target
                heapq.heappush(heap, [i, target])

BFS()
print(visited[end])