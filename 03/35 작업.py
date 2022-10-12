import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
time = [0] * (N+1)
M_lst = [[] for _ in range(N+1)]

inDegree = [0 for _ in range(N+1)]
DP = [0 for _ in range(N+1)]

for i in range(1, N+1):
    A = list(map(int, input().split()))
    time[i] = A[0]
    # 간선이 있으면 실행
    inDegree[i] = A[1]
    for j in range(A[1]):
        M_lst[A[j+2]].append(i)

Q = deque()

for i in range(1, N+1):
    if inDegree[i] == 0:
        Q.append(i)
        DP[i] = time[i]
# init_time = max(DP)
# print(time, M_lst, N, inDegree, DP, Q)

while Q:
    now_N = Q.popleft()
    for i in M_lst[now_N]:
        inDegree[i] -= 1
        DP[i] = max(DP[now_N] + time[i], DP[i])
        if inDegree[i] == 0:
            Q.append(i)

print(max(DP))