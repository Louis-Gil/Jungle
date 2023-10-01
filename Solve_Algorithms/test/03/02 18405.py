import sys
import heapq
input = sys.stdin.readline

line, virus_num = map(int,input().split())
graph = [[] for _ in range(line+1)]
graph[0]=[0,0,0,0]
for i in range(1,line+1):
    A = list(map(int,input().split()))
    graph[i] = [0]+A
want_time, want_y, want_x = map(int,input().split())
# print(line,virus_num, graph)
# print(want_time, want_y, want_x)


dx = [0,0,1,-1]
dy = [1,-1,0,0]
Q = []
tempQ = []
for j in range(1, line+1):
    for k in range(1, line+1):
        if graph[j][k] != 0:
            heapq.heappush(Q, [graph[j][k], j, k])
# print(Q)
for i in range(want_time):
    while Q:
        A, Y, X =heapq.heappop(Q)
        for i in range(4):
            cy = Y + dy[i]
            cx = X + dx[i]
            if 0<cy<=line and 0<cx<=line and graph[cy][cx]==0:
                graph[cy][cx]=A
                heapq.heappush(tempQ, [A,cy,cx])
    Q = tempQ[:]
    tempQ =[]
print(graph[want_y][want_x])