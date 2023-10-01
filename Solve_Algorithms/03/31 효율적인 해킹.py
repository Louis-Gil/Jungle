import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    queue = deque()
    queue.append(num)
    visit = [0 for _ in range(computer_num+1)]
    visit[num] = 1
    cnt = 1
    while queue:
        st = queue.popleft()
        for i in graph[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                queue.append(i)
    return cnt

computer_num, line_num = map(int, input().split())
graph = [[] for _ in range(computer_num+1)]

for _ in range(line_num):
    A, B = map(int, input().split())
    graph[B].append(A)
# print(computer_num, graph)

result = []
max_cnt = 0
result = [0]*(computer_num+1)
for i in range(1, computer_num+1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)
