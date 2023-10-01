# https://www.acmicpc.net/problem/1707
import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
testcase = int(input())

def dfs(start, group):
    visited1[start] = group
    for i in graph[start]:
        if visited1[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited1[i] == visited1[start]:
            return False
    return True

def bfs(start, group):
    queue = deque([start])
    visited2[start] = group
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = -visited2[x]
            elif visited2[i] == visited2[x]:
                return False
    return True
        
for _ in range(testcase):
    point_num, line_num = map(int, input().split())
    graph = [[] for _ in range(point_num+1)]
    for _ in range(line_num):
        point1, point2 = map(int, input().split())
        graph[point1].append(point2)
        graph[point2].append(point1)
    visited1 = [0] * (point_num + 1)
    visited2 = [0] * (point_num + 1)
    
    result = True
    for i in range(1, point_num+1):
        if visited1[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    print('YES' if result else "NO")

    # result = True
    # for i in range(1, point_num+1):
    #     if not visited2[i]:
    #         result = bfs(i, 1)
    #         if not result:
    #             break
    # print('YES' if result else "NO")