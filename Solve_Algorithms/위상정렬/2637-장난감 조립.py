# https://www.acmicpc.net/problem/2637
import sys
from collections import deque
input = sys.stdin.readline

Toy_num = int(input())
line_num = int(input())
graph = [[] for _ in range(Toy_num+1)]
indegree = [0 for _ in range(Toy_num+1)]
for i in range(1, line_num+1):
    X, Y, K = map(int, input().split())
    graph[Y].append((X,K))
    indegree[X] += 1
need_arr = [[0]*(Toy_num+1) for _ in range(Toy_num+1)]
q = deque()

for i in range(1, Toy_num+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    low_toy = q.popleft()
    for next, next_need in graph[low_toy]:
        if need_arr[low_toy].count(0) == Toy_num+1:
            need_arr[next][low_toy] += next_need
        else:
            for i in range(1, Toy_num+1):
                need_arr[next][i] += need_arr[low_toy][i] * next_need
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
for x in enumerate(need_arr[Toy_num]):
    if x[1] > 0:
        print(*x)