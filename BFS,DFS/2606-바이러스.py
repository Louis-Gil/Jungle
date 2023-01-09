# https://www.acmicpc.net/problem/2606
import sys

input = sys.stdin.readline
cpt = int(input())
line = int(input())
arr = [[0] * (cpt + 1) for _ in range(cpt + 1)]
for i in range(1, line+1):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(start):
    if arr[start][0] == 1:
        return
    arr[start][0] = 1
    for i in range(1, cpt+1):
        if arr[start][i] == 1:
            dfs(i)

dfs(1)
answer = 0
for i in range(1, cpt+1):
    if arr[i][0] == 1:
        answer += 1
        
print(answer-1)