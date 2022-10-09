import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start, group):
    global error

    if error:
        return

    visit[start] = group

    for i in graph[start]:
        if not visit[i]:
            dfs(i, -group)
        elif visit[start] == visit[i]:
            error = True
            return

test_num = int(input())
for _ in range(test_num):
    point, line = map(int, input().split())

    graph = [[] for _ in range(point+1)]
    visit = [False] * (point+1)
    error = False

    for _ in range(line):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    
    for i in range(1, point+1):
        if not visit[i]:
            dfs(i, 1)
            if error:
                break

    if error:
        print('NO')
    else :
        print('YES')

    print(test_num, point, line, graph, visit)




