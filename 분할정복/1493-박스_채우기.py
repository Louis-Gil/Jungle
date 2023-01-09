# https://www.acmicpc.net/problem/1493
import sys
input = sys.stdin.readline


length, width, height = map(int, input().split())
total = length * width * height
N = int(input())
cube = [tuple(map(int, input().split())) for _ in range(N)]
cube.sort(reverse=True)

answer, total_now = 0, 0
for cube_idx, cube_cnt in cube:
    total_now *= 8
    cube_len = 2**cube_idx
    
    cnt_limit = (length // cube_len) * (width // cube_len) * (height // cube_len) - total_now
    cnt_limit = min(cube_cnt, cnt_limit)
    
    answer += cnt_limit
    total_now += cnt_limit

if total_now == total:
    print(answer)
else:
    print(-1)