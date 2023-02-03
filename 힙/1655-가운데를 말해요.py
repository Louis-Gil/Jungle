# https://www.acmicpc.net/problem/1655
import heapq
import sys
input = sys.stdin.readline

leftheap = []
rightheap = []

N = int(input())
for i in range(N):
    integer = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -integer)
    else:
        heapq.heappush(rightheap, integer)
    
    if rightheap and -leftheap[0] > rightheap[0]:
        heapq.heappush(leftheap, -heapq.heappop(rightheap))
        heapq.heappush(rightheap, -heapq.heappop(leftheap))
    print(-leftheap[0])