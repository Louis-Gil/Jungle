import sys
from collections import deque


# 물이 차있는 지역 bfs 탐색
def _water():
    global water
    temp_water = [] # 물이 차 있는 지역

    # 물이 차있는 모든 지역을 탐색
    while water:
        x, y = water.popleft()

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고
            if 0 <= nx < r and 0 <= ny < c:
                # 이동할 수 있는 곳이라면 물이 차게된다.
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"
                    visited[nx][ny] = -1
                    temp_water.append([nx, ny]) # 물이 찬 지역을 임시 큐에 저장

    # 물이 찰 수 있는 지역이 물로 다 채워졌다면
    # 임시 큐에 있는 다음 탐색할 곳을 큐에 추가
    for a, b in temp_water:
        water.append([a, b])


# 고슴도치의 이동 bfs 탐색
def bfs():
    global queue

    while queue:
        temp_queue = [] # 임시 큐

        # 고슴도치가 이동할 수 있는 모든 곳을 탐색
        while queue:

            x, y = queue.popleft()

            # 물이 아니고 돌이 아니라면
            if graph[x][y] != "*" and graph[x][y] != "X":

                # 상/하/좌/우 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 탐색하는 곳이 범위 내에 있다면
                    if 0 <= nx < r and 0 <= ny < c:

                        # 비버의 굴이라면 비버의 굴까지 걸리는 이동 횟수 리턴
                        if graph[nx][ny] == "D":
                            return visited[x][y] + 1

                        # 비어 있는 곳이고 탐색하지 않은 곳이라면 탐색
                        elif graph[nx][ny] == "." and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1 # 탐색하기까지 걸린 이동 횟수 초기화
                            temp_queue.append([nx, ny]) # 임시 큐에 탐색할 곳을 추가

        # 고슴도치가 현재 이동할 수 있는 곳을 모두 이동했다면
        # 임시 큐에 있는 다음 탐색할 곳을 큐에 추가
        for a, b in temp_queue:
            queue.append([a, b])

        # 물이 차있는 지역 증가
        _water()

    # 고슴도치가 목적지까지 이동할 수 없다면 "KAKTUS" 리턴
    return "KAKTUS"


r, c = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)] # 이동 횟수, 탐색여부

queue = deque([])
water = deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 그래프를 탐색해 고슴도치의 위치와 물의 위치를 찾는다.
for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            queue.append([i, j])

        elif graph[i][j] == "*":
            water.append([i, j])

# bfs 탐색
print(bfs())