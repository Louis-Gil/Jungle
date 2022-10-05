import heapq
import sys
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())

leftHeap = []
rightHeap = []

for i in range(num):
    temp = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -temp)
    else:
        heapq.heappush(rightHeap, temp)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])