import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    A=list(map(int, input().split()))
    time[i]=A[0]
    for j in A[1:]:
        if j != -1:
            graph[j].append(i)
            in_degree[i]+=1
# print("time, in_degree", time, in_degree)
# print("graph", graph)

# graph 건물에서 다음 건물 화살표
# time 각 건물 짓는 시간
# in_degree 화살표 받는 수

Q = deque()
# result 각 건물 걸리는 시간
result = [0]*(N+1)

for i in range(1, N+1):
    if in_degree[i] == 0:
        Q.append(i)
# print("result, Q", result, Q)

while Q:
    now_N = Q.popleft()
    result[now_N] += time[now_N]
    for i in graph[now_N]:
        in_degree[i] -=1
        result[i] = max(result[i], result[now_N])
        if in_degree[i] == 0:
            Q.append(i)
            
            # print('hi', now_N)
# 2가지 방법? 앞과 뒤
# 만약 전 타임의 도시에 현시간 더한게 크면 업데이트
for i in range(1, N+1):
    print(result[i])