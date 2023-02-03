# https://www.acmicpc.net/problem/11279
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    X = int(input())
    if X != 0:
        heapq.heappush(heap, -X)
        continue
    if len(heap) == 0:
        print(0)
    else:
        print(-heapq.heappop(heap))
    