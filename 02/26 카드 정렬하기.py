import heapq
import sys
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
heapq_lst = []
result = 0
for i in range(num):
    heapq.heappush(heapq_lst, int(sys.stdin.readline()))

for i in range(num-1):
    tempA = heapq.heappop(heapq_lst)
    tempB = heapq.heappop(heapq_lst)
    result = result + tempA + tempB
    heapq.heappush(heapq_lst, tempA+tempB)
    # print(heapq_lst)
print(result)