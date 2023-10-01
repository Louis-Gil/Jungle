# https://www.acmicpc.net/problem/1932
import sys

input = sys.stdin.readline

N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(ARR[i])):
        if j == 0:
            ARR[i][j]=ARR[i][j]+ARR[i-1][j]
        elif j == len(ARR[i])-1:
            ARR[i][j]=ARR[i][j]+ARR[i-1][j-1]
        else:
            ARR[i][j]=max(ARR[i-1][j-1], ARR[i-1][j]) + ARR[i][j]
print(max(ARR[N-1]))