# https://www.acmicpc.net/problem/2206
import sys

N, M = map(int, sys.stdin.readline().split())
dist = []

for i in range(N):
    dist.append(list(map(int, sys.stdin.readline().strip())))
    
print (dist)

def break_wall(row, col):
    pass
    

break_wall(1,1)
