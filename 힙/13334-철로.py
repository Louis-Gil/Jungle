# https://www.acmicpc.net/problem/13334
import sys
import heapq
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    line.append(list(map(int, input().split())))
korail = int(input())

roads = []
for i in line:
    house, office = i
    if abs(house - office) <= korail:
        i = sorted(i)
        roads.append(i)
roads.sort(key = lambda x:x[1])

answer = 0
heap = []
for i in roads:
    if not heap:
        heapq.heappush(heap, i)
    else:
        while heap[0][0] < i[1] - korail:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    answer = max(answer, len(heap))
print(answer)