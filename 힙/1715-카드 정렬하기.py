# https://www.acmicpc.net/problem/1715
import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

if N == 1:
    print(0)
    exit()

result = 0
for _ in range(N-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    result += a + b
    heapq.heappush(arr, a+b)
print(result)