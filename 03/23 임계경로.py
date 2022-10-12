import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
M_lst = [[] for _ in range(N+1)]
Time =  [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
DP = [0 for _ in range(N+1)]

for i in range(M):
    A,B,C=map(int,input().split())
    M_lst[A].append(B)
    Time[A].append(C)
    inDegree[B] += 1
start, end = map(int,input().split())

Q = deque()
for i in range(1, N+1):
    if inDegree[i] == 0:
        Q.append(i)
        DP[i] = Time[i]
print(N, M, M_lst, Time, inDegree, DP, start, end, Q)

while Q:
    now_N = Q.popleft()
    for i in range(1, len(M_lst[now_N])+1):
        inDegree[M_lst[now_N][i]] -= 1
        DP[M_lst[now_N][i]] = max(DP[now_N] + Time[i], DP[i])
        if inDegree[i] == 0:
            Q.append(i)
print(DP)