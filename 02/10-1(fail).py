# 좌표 하나를 선택한다
# 0. X좌표에서 라이플 거리 미만에 있는 점만 불러오기
#   y좌표에서 라이플 거리 미만에 있는 점만 불러오기
# 1. 좌표의 라이플 거리에 있는 점 1개 찾기 
# 2. 라이플 재생성 -> 0번으로 

import sys
sys.stdin = open('02\input.txt', 'r')

target = int(sys.stdin.readline())
xcor = [[] for x in range(10001)]
ycor = [[] for x in range(10001)]
lst = []
# print(xcor)

for i in range(target):
    x_dot, y_dot = list(map(int, sys.stdin.readline().split()))
    lst.append([x_dot, y_dot])
    xcor[y_dot].append([x_dot, y_dot])
    ycor[x_dot].append([x_dot, y_dot])
rifle = 1e9
print(xcor[10], ycor[10], lst)
print(xcor[-1])

def cloeset():
    for i in range(target):
        temp_x = lst[i][0]
        temp_y = lst[i][1]
        if lst[i][0] - rifle < 0:
            temp_x = 0
        elif lst[i][1] - rifle < 0:
            temp_y = 0
        elif lst[i][0] + rifle > 10001:
            temp_x = 10001
        elif lst[i][1] + rifle > 10001:
            temp_y = 10001
        
        temp_x_lst = lst[:lst[i][0]]

        print(lst[i], lst[i][0], lst[i][1], temp_x, temp_y)
        

        # xcor_temp = xcor[]
        # temp_list = []
        # lst[i]

cloeset()