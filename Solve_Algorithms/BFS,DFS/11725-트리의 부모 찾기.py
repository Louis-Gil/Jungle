# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**8)
from collections import deque
input = sys.stdin.readline

node_num = int(input())
tree = [[] for _ in range(node_num+1)]
for i in range(node_num-1):
    point1, point2 = map(int, input().split())
    tree[point1].append(point2)
    tree[point2].append(point1)
visit_lst1 = [0] * (node_num + 1)
visit_lst2 = [0] * (node_num + 1)
# print(tree)

# result_lst1 = [0] * (node_num+1)
# def dfs(v):
#     visit_lst1[v] = 1
#     for i in tree[v]:
#         if not visit_lst1[i]:
#             result_lst1[i] = v
#             dfs(i)
# dfs(1)
# print(*result_lst1[2:], sep='\n')

def bfs(v):
    queue = deque([v])
    visit_lst2[v] = 1
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if visit_lst2[i] == 0:
                queue.append(i)
                visit_lst2[i] = v
bfs(1)
print(*visit_lst2[2:], sep='\n')