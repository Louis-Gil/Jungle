import sys
import heapq
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dia_num, bag_num = map(int, input().split())
dia_lst = []
for i in range(dia_num):
    dia_lst.append(list(map(int, input().split())))
heapq.heapify(dia_lst)

bag_lst = []
for i in range(bag_num):
    bag_lst.append(int(input()))
bag_lst.sort()

result = 0
temp_lst = []
for i in range(bag_num):
    while True:
        if dia_lst and dia_lst[0][0] <= bag_lst[i]:
            _, B = heapq.heappop(dia_lst)
            heapq.heappush(temp_lst, -B)
        else:
            if temp_lst:
                temp = heapq.heappop(temp_lst)
                result += temp
            break
print(-result)