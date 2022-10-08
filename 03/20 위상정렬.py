import sys
from collections import deque
input = sys.stdin.readline

student_num, test_num = map(int, input().split())

graph = [[] for _ in range(student_num+1)]
inDegree = [0 for _ in range(student_num+1)]
queue = deque()
answer = []

for i in range(test_num):
    big, small = map(int, input().split())
    graph[big].append(small)
    inDegree[small] += 1

# print(graph)
for i in range(1, student_num+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)
print(*answer)

