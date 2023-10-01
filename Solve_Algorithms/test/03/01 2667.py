import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]
lst[0] = ['0', '0', '0', '0', '0', '0', '0', '0']
for i in range(1, N+1):
    A = list(map(str, input().strip()))
    lst[i] = ['0'] + A

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(y, x):
    global temp
    lst[y][x] = '0'
    temp += 1
    for i in range(4):
        cy = y+dy[i]
        cx = x+dx[i]
        if 0<cx<=N and 0<cy<=N and lst[cy][cx] =='1':
            dfs(cy, cx)

count = 0
temp = 0
result = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if lst[i][j] != '0':
            count+=1
            dfs(i, j)
            result.append(temp)
            temp=0
result.sort()
print(len(result))
print(*result, sep="\n")