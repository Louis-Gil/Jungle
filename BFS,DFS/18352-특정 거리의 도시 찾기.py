# https://www.acmicpc.net/problem/18352
import sys
from collections import deque
input = sys.stdin.readline

city_num, road_num, distance, start = map(int, input().split())
graph = [[] for _ in range(city_num+1)]
for i in range(road_num):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [0] * (city_num+1)
result = []

def bfs(start, distance):
    queue = deque()
    queue.append([start, 1])
    visited[start] = 1
    while queue:
        city, dist = queue.popleft()
        if dist == distance+1:
            result.append(city)
        for i in graph[city]:
            if visited[i] == 0:
                visited[i] = dist + 1
                queue.append([i, dist+1])


bfs(start, distance)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')

# import sys
# from collections import deque
# input = sys.stdin.readline

# # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# N, M, K, X = map(int, input().split())
# M_lst = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     M_lst[A].append(B)
# # print(N,M,K,X,M_lst)


# visit = [0]* (N+1)
# distance = [0] * (N+1)

# def BFS(start):
#     answer = []
#     Q = deque([start])
#     visit[start] = True
#     while(Q):
#         city = Q.popleft()
#         for i in M_lst[city]:
#             if visit[i] == 0:
#                 visit[i] = 1
#                 Q.append(i)
#                 distance[i] = distance[city] + 1
#                 if distance[i] == K:
#                     answer.append(i)
#     if len(answer) == 0:
#         print(-1)
#     else :
#         answer.sort()
#         for i in answer:
#             print(i, end='\n')
    


# BFS(X)