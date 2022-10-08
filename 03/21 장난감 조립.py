import sys
from collections import deque
input = sys.stdin.readline

part_num = int(input())
line_num = int(input())

graph = [[] for _ in range(part_num+1)]
inDegree = [0 for _ in range(part_num+1)]

for i in range(line_num):
    a, b, c = map(int, input().split())
    graph[b].append((a,c))
    inDegree[a] += 1

needs = [[0]*(part_num+1) for _ in range(part_num+1)]
q = deque()

for i in range(1, part_num+1):
    if inDegree[i] == 0:
        q.append(i)
print(part_num, line_num)
print(graph)
print(inDegree)
print(needs)
print(q)
while q:
    now = q.popleft()
    for next, next_need in graph[now]:
        if needs[now].count(0) == part_num + 1:
            needs[next][now] += next_need
        else:
            for i in range(1, part_num+1):
                needs[next][i] += needs[now][i] * next_need
        inDegree[next] -= 1
        if inDegree[next] == 0:
            q.append(next)
for x in enumerate(needs[part_num]):
    if x[1] > 0:
        print(*x)
