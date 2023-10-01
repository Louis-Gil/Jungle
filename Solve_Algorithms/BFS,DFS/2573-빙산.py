# https://www.acmicpc.net/problem/2573
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
"""
날짜를 1 증가한다
반복문으로 빙산 한개를 찾는다, break (count1)
dfs, bfs를 통해 빙산을 돌면서 녹일맵을 만든다 (count2)
count1과 count2가 다르면 break
빙산을 녹인다
34% 시간초과
"""

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

day = 0

def find():
    ice = [None, None]
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] != 0:
                ice = [i,j]
                count += 1
    return ice, count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_map(y, x):
    global count2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주변이 물인경우
        if graph[ny][nx] == 0:
            melt_map[y][x] += 1
        # 주변이 빙산인경우
        elif not visited[ny][nx]:
            count2 += 1
            visited[ny][nx] = 1
            dfs_map(ny, nx)
    return
    
def melt():
    for i in range(row):
        for j in range(col):
            graph[i][j] = max(0, graph[i][j] - melt_map[i][j])

while True:
    ice, count1 = find()
    if count1 == 1:
        break
    count2 = 1
    melt_map = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    visited[ice[0]][ice[1]] = 1
    dfs_map(ice[0], ice[1])
    if count1 != count2:
        break
    day += 1
    melt()
print(day)




# import sys
# input = sys.stdin.readline


# def melt():
#     melting_area = {}  # 녹일 곳
#     dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
#     visited = [[0] * M for _ in range(N)]  # 방문
#     stack = []
#     stack.append(iceberg[0])
#     selected_iceberg = 0  # 선택된 빙산들 ( 나중에 전체 빙산과 비교해서 한덩어리인지 확인 )
#     visited[iceberg[0][0]][iceberg[0][1]] = 1
#     while stack:
#         x, y = stack.pop()
#         selected_iceberg += 1
#         melting_cnt = 0
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if arctic[nx][ny] and not visited[nx][ny]:  # 옆이 육지이면 다음 탐색
#                 stack.append((nx, ny))
#                 visited[nx][ny] = 1
#             elif arctic[nx][ny] == 0:  # 옆이 바다이면 녹이는 카운트
#                 melting_cnt += 1

#         melting_area[(x, y)] = melting_cnt

#     # 녹이기
#     new_iceberg = []  # 새로운 빙산으로 바꾸기 위해
#     for key, value in melting_area.items():
#         i, j = key
#         arctic[i][j] = max(0, arctic[i][j] - value)
#         if arctic[i][j] > 0:
#             new_iceberg.append((i, j))

#     return selected_iceberg, new_iceberg


# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     arctic = [list(map(int, input().split())) for _ in range(N)]

#     # 빙산만 찾기
#     iceberg = []
#     for i in range(N):
#         for j in range(M):
#             if arctic[i][j]:
#                 iceberg.append((i, j))

#     answer = 0  # year
#     while True:
#         # 녹이기
#         selected_cnt, new_iceberg = melt()
#         # 한덩어리인지
#         if selected_cnt != len(iceberg):
#             break

#         if selected_cnt == 0 or len(new_iceberg) == 0:
#             answer = 0
#             break
#         iceberg = new_iceberg[:]

#         answer += 1

#     print(answer)
 