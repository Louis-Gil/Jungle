import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(sp, ep, count):
    global result
    visit[sp] = True

    if sp == ep:
        result = count
        return 
    for i in graph[sp]:
        if not visit[i]:
            dfs(i, ep, count+1)

people_num = int(input())
SP, EP = map(int, input().split())
line_num = int(input())

graph = [[] for _ in range(people_num+1)]
visit = [False] * (people_num+1)
for _ in range(line_num):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
result = -1

dfs(SP, EP, 0)
print(result)
# print(people_num, SP, EP, line_num, graph, visit)