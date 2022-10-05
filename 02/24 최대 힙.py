import heapq as hq
import sys
sys.stdin = open('02\input.txt', 'r')

field_num = int(sys.stdin.readline())
hip_lst = []

for i in range(field_num):
    temp = (int(sys.stdin.readline()))
    if temp != 0:
        hq.heappush(hip_lst, (-temp, temp))
        print(hip_lst)
    else : #temp == 0
        if len(hip_lst) >= 1:
            print(hq.heappop(hip_lst)[1])
        else :
            print(0)
    # print(temp, hip_lst)