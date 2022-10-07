import sys
sys.setrecursionlimit(10000)


def dfs(x, y, type):

    done.append((x, y))

    # 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny < N) and ((nx, ny) not in done):
            # 정상인
            if type == 0 and colors[nx][ny] == colors[x][y]:
                dfs(nx, ny, 0)
            # 적록색맹
            elif type == 1 and colors[nx][ny] == colors[x][y]:
                dfs(nx, ny, 1)


N = int(input())
colors = [list(input()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 정상인인 경우
done = []
cnt_1 = 0

for i in range(N):
    for j in range(N):
        if (i, j) not in done:
            dfs(i, j, 0)
            cnt_1 += 1


# 적록색맹인 경우
for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

done = []
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if (i, j) not in done:
            dfs(i, j, 1)
            cnt_2 += 1

print(cnt_1, cnt_2)