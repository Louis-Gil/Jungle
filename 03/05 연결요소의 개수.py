import sys
from collections import deque
# sys.stdin = open('03\input.txt', 'r')

point_num, line_num = list(map(int, sys.stdin.readline().split()))


graph = [[0] * (point_num+1) for _ in range(point_num+1)]
for i in range(line_num):
    A, B = (map(int, sys.stdin.readline().split()))
    graph[A][B] = graph[B][A] = 1

visit_lst = [0] * (point_num + 1)
# print(point_num, line_num, graph)

def bfs(num):
    Q = deque()
    Q.append(num)
    visit_lst[num] = 1
    while Q:
        num = Q.popleft()
        # 프린트
        for i in range(1, point_num+1):
            if visit_lst[i] == 0 and graph[num][i] == 1:
                visit_lst[i] = 1
                Q.append(i)

result = 0
for i in range(1, point_num+1):
    if visit_lst[i] == 0:
        result += 1
        bfs(i)

print(result)