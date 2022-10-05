import sys
from bisect import insort
from collections import deque
sys.stdin = open('02\input.txt', 'r')

circle_num = int(sys.stdin.readline())
circle_lst =[]
for i in range(circle_num):
    A, B = list(map(int, sys.stdin.readline().split()))
    A, B = A - B, A + B
    circle_lst.append([A, B])
circle_lst.sort()
# print(circle_lst, circle_lst[0][0])

result = 1
result_lst = deque()
for i in circle_lst:
    if not result_lst: #리스트가 비었을때
        result_lst.append(i)
    else:#리스트가 안비었을때
        if (result_lst[-1][0] == i[0]): #리스트 마지막 0,2보다 큰 0,4가 들어올때
            result_lst.appendleft(i)
        elif result_lst[-1][1] == i[0]: #리스트 마지막 04, 0,2 이후 2,3, 2,4 들이 들어올때 04 46/ 원 안으로 들어오거나 원 밖으로
            if result_lst[0][1] < i[1]:
                result_lst.clear()
                result_lst.append(i)
            elif result_lst[0][1] > i[1]:
                insort(i, result_lst)
            else : #같을때
                result_lst.append(i)
                result += 1
        else : #리스트 마지막 0,2보다 큰 3,4, 
            result_lst.clear()
            result_lst.append(i)
    result += 1
    # 끝의 오른쪽이 맨 앞의 오른쪽과 같나 비교
    # 1. 끝의 오른쪽과 들어오는 왼쪽이 같을때
    # 2. 끝의 오른쪽과 들어오는 왼쪽이 다를때



print(result)
