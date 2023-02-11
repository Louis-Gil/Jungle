# https://www.acmicpc.net/problem/2252
import sys
from collections import deque
input = sys.stdin.readline

people_num, line_num = map(int, input().split())
graph = [[] for _ in range(people_num+1)]
indegree = [0 for _ in range(people_num+1)]
for i in range(line_num):
    small, big = map(int, input().split())
    graph[small].append(big)
    indegree[big] += 1

result = []
def topology_sort():
    queue = deque()
    for i in range(1, people_num+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        tmp = queue.popleft()
        result.append(tmp)
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
topology_sort()
print(*result)