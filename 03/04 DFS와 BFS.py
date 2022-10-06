from collections import deque
import sys
# sys.stdin = open('03\input.txt', 'r')
number, line_num, start_num = list(map(int, sys.stdin.readline().split()))

graph = [[0] * (number+1) for _ in range(number+1)]
visit_lst1 = [0] * (number + 1)
visit_lst2 = [0] * (number + 1)

for i in range(line_num):
    A, B = (map(int, sys.stdin.readline().split()))
    graph[A][B] = graph[B][A] = 1
# print(number, start_num, graph)

def bfs(v):
    q = deque()
    q.append(v)
    visit_lst1[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, number+1):
            if visit_lst1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_lst1[i] = 1

def dfs(v):
    visit_lst2[v] = 1
    print(v, end = " ")
    for i in range(1, number + 1):
        if visit_lst2[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(start_num)
# print(visit_lst2)
print()

bfs(start_num)
# print(visit_lst1)

