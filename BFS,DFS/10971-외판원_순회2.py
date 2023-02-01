# https://www.acmicpc.net/problem/10971

import sys

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize #출력할 최소값 정의

def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value
    
    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(N):
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value + travel_cost[next][i], visited)
            visited.pop()

#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)

# from itertools import permutations

# n = int(input())
# Get_list = []
# for i in range(n):
#     Get_list.append(list(map(int, input().split())))
# # print(n, Get_list)

# result = 0
# route = list(permutations(list(range(n))))
# # print(route[0])
# # print(Get_list[0][1])

# for i in route:
#     sum = 0
#     for j in range(n):
#         num = Get_list[i[j]][i[(j+1)%n]]
#         if num == 0:
#             break
#         sum += num
#     if result == 0:
#         result = sum
#     elif result > sum:
#         result = 0

# print(result)