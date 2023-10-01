import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
weight = [[0]*(N+1) for _ in range(N+1)]
in_degree = [0] * (N+1)
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    if weight[a][b] <c:
        weight[a][b] = weight[b][a] = c
start, end = map(int,input().split())
# print(weight, in_degree, graph, weight)

Q = []
for i in range(1,N+1):
    if graph[start][i] == 1:
        heapq.heappush(Q, [-weight[start][i], i])
# print(Q)

while Q:
    now_weight, now_i = heapq.heappop(Q)
    now_weight *= -1
    if now_i == end:
        print(now_weight)
        break
    for i in range(1,N+1):
        if graph[now_i][i] == 1:
            heapq.heappush(Q, [-weight[now_i][i], i])

# print(Q)
#무게를 바이너리 서치?