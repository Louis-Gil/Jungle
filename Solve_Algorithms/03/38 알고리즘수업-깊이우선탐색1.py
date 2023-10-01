import sys
sys.setrecursionlimit(10**9)
# from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(1,M+1):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
visited = [0]*(N+1)
count = 1
# print(N,M,R,graph)

def dfs(num):
    global count
    visited[num] = count
    graph[num].sort()
    for i in graph[num]:
        if visited[i]==0 :
            count += 1
            dfs(i)


dfs(R)

for i in range(1, N+1):
    print(visited[i])