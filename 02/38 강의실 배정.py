import sys
import heapq
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
lst = []
for i in range(num):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(reverse=True)


study = []
heapq.heappush(study, lst.pop()[1])
for i in range(num-1):
    if study[0] <= lst[-1][0]:
        heapq.heappushpop(study, lst.pop()[1])
    else :
        heapq.heappush(study, lst.pop()[1])
print(len(study))