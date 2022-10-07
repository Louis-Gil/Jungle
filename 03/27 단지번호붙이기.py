import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

graph_num = int(input())

graph = [list(map(int, input())) for _ in range(graph_num)]
# print(graph_num, graph)

def dfs(num1, num2):
    global count
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[num1][num2] = 0
    for i in range(4):
        cx = num1 + dx[i]
        cy = num2 + dy[i]
        if 0 <= cx < graph_num and 0 <= cy < graph_num and graph[cx][cy] == 1:
            count += 1
            dfs(cx, cy)
    
result = []

for i in range(graph_num):
    for j in range(graph_num):
        if graph[i][j] == 1:
            count = 1
            dfs(i, j)
            result.append(count)
result.sort()
print(len(result))
print(*result, sep="\n")