import heapq
import sys
sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
person_lst = []
for i in range(num):
    person_lst.append(list(map(int, sys.stdin.readline().split())))
korail = int(sys.stdin.readline())
roads = []
for i in person_lst:
    house, office = i
    if abs(house - office) <= korail:
        i = sorted(i)
        roads.append(i)
roads.sort(key = lambda x:x[1])
print(num, korail, roads)

answer = 0
heap = []
for i in roads:
    if not heap:
        heapq.heappush(heap, i)
    else :
        while heap[0][0] < i[1] - korail:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    answer = max(answer, len(heap))

print(answer)