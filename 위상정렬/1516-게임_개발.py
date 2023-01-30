# https://www.acmicpc.net/problem/1516
import sys
from collections import deque

input = sys.stdin.readline
arr_num = int(input())

building = [[] for _ in range(arr_num+1)]
indegree = [0] * (arr_num+1)
cost = [0] * (arr_num+1)

for i in range(1, arr_num + 1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    building_data = data[1:]
    
    for j in building_data:
        building[j].append(i)
        indegree[i] += 1
        
def topology_sort():
    result = [0] * (arr_num+1)
    q = deque()

    for i in range(1, arr_num+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += cost[now]
        for b in building[now]:
            indegree[b] -= 1
            result[b] = max(result[b], result[now])
            if indegree[b] == 0:
                q.append(b)
    return result
    
answer = topology_sort()
for i in range(1, arr_num+1):
    print(answer[i])