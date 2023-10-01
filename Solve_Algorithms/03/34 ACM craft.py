import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for k in range(T):
    N, M = map(int, input().split())
    Time = [0] + list(map(int, input().split()))
    M_lst = [[] for _ in range(N+1)]
    inDegree = [0 for _ in range(N+1)]
    DP = [0 for _ in range(N+1)]

    for i in range(M):
        A, B = map(int, input().split())
        M_lst[A].append(B)
        inDegree[B] += 1

    target = int(input())
    # print(N, M, Time, M_lst, target, inDegree, DP)


    Q = deque()

    for i in range(1, N+1):
        if inDegree[i] == 0:
            Q.append(i)
            DP[i] = Time[i]

    while Q:
        now_N = Q.popleft()
        for i in M_lst[now_N]:
            inDegree[i] -= 1
            DP[i] = max(DP[now_N] + Time[i], DP[i])
            if inDegree[i] == 0:
                Q.append(i)

    print(DP[target])



