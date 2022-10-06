import sys
# sys.stdin = open('03\input.txt', 'r')

computer_num = int(sys.stdin.readline())
line_num = int(sys.stdin.readline())

graph = [[0]*(computer_num+1) for _ in range(computer_num+1)]
for i in range(line_num):
    A, B = (map(int, sys.stdin.readline().split()))
    graph[A][B] = graph[B][A] = 1

visit_line = [0] * (computer_num+1)
# print(graph, computer_num, line_num)

count = -1
def dfs(num):
    global count
    visit_line[num] = 1
    count += 1
    for i in range(1, computer_num+1):
        if visit_line[i] == 0 and graph[num][i] == 1:
            dfs(i)
    

dfs(1)
print(count)