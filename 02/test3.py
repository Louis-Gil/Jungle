from bisect import bisect_right
from collections import deque
import sys
# sys.stdin = open('02\input.txt', 'r')

field_num = int(sys.stdin.readline())
hip_lst = deque()

for i in range(field_num):
    temp = (int(sys.stdin.readline()))
    if temp != 0:
        try :
            bi_tmp = bisect_right(hip_lst, temp)
            hip_lst.insert(bi_tmp, temp)
            # j = 1
            # while temp < hip_lst[j]:
            #     j = 2**j -2
        except:
            hip_lst.append(temp)
    else : #temp == 0
        try :
            print(hip_lst.pop())
        except :
            print(0)
    # print(temp, hip_lst)