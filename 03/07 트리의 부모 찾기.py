import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node_num = int(input())
graph = [[] for _ in range(node_num+1)]
visit_lst = [0] * (node_num + 1)
result = [0] * (node_num+1)

for i in range(node_num-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
# print(node_num, graph)


def dfs(node):
    visit_lst[node] = 1
    for i in graph[node]:
        if not visit_lst[i]:
            result[i] = node
            dfs(i)

for i in range(node_num+1):
    graph[i].sort()
dfs(1)
print(*result[2:], sep='\n')