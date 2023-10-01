import sys
# sys.stdin = open('03\input.txt', 'r')
sys.setrecursionlimit(10000)

def find_land(row1, col1):
    dx = [1, -1 , 0 , 0, 1, 1, -1, -1]
    dy = [0, 0 , 1, -1, 1, -1, 1, -1]
    graph[row1][col1] = 0
    for i in range(8):
        x = row1 + dx[i] #row
        y = col1 + dy[i] #col
        if 0 <= x < row and 0 <= y < col and graph[x][y] == 1:
            find_land(x, y)


while True:
    col, row = map(int, sys.stdin.readline().split())
    if row == 0 and col == 0:
        break
    graph = []
    for _ in range(row):
        graph.append(list(map(int, sys.stdin.readline().split())))
    count = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                count += 1
                find_land(i, j)

    print(count)



