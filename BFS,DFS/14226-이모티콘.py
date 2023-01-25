# https://www.acmicpc.net/problem/14226
from collections import deque

num = int(input())
dist = [[-1] * (num+1) for _ in range(num+1)]
q = deque()
q.append((1,0))
dist[1][0] = 0

while q:
    s,c = q.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= num and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c,c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1,c))
answer = -1
for i in range(num+1):
    if dist[num][i] != -1:
        if answer == -1 or answer > dist[num][i]:
            answer = dist[num][i]
print(answer)