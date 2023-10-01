# 테스트 케이스 통과
# 시간 초과

from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
b_arr = [list(map(int, input().split())) for x in range(n)]


def skyline(b_arr):
    arr = [[True, x[0], x[1]] for x in b_arr] + [[False, x[2], x[1]] for x in b_arr]
    arr.sort(key=lambda x: (x[1], x[0], x[2]))
    h = 0
    heap = []
    stack = []
    result = []

    for i, b in enumerate(arr):
        if b[0]:
            heappush(heap, -b[2])
            if b[2] > h:
                h = b[2]
                result.append([b[1], h])

            stack.append(b)

        else:

            if b[2] == h:
                heappop(heap)

                if heap:
                    h = -heap[0]
                else:
                    h = 0

                result.append([b[1], h])
            else:
                if -b[2] in heap:
                    heap.remove(-b[2])
                    heapify(heap)

            stack.pop()

    return result


for i in skyline(b_arr):
    for j in i:
        print(j, end=" ")