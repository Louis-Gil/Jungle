import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]

for i in range(M):
    # 3 1 4 3
    # 1에 4를 넣고 4에 카운트 추가
    A = list(map(int, input().split()))
    for j in range(1, A[0]):
        graph[A[j]].append(A[j+1])
        inDegree[A[j+1]] += 1
# print(N, M, graph, inDegree)

Q = deque()
result = []

for i in range(1, N+1):
    if inDegree[i] == 0:
        Q.append(i)
        result.append(i)

while Q:
    now_N = Q.popleft()
    for i in graph[now_N]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            Q.append(i)
            result.append(i)
if len(result) == N:
    print(*result, sep="\n")
else: print(0)