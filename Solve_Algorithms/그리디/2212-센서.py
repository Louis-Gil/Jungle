# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline
# 1-3 6-7-9
# 3 6-7-8 10-12 14-15 18-20

N = int(input())
K = int(input())
Arr = sorted(list(map(int, input().split())))

interval = []
for i in range(N-1):
    interval.append(Arr[i+1]-Arr[i])
interval.sort()

if K >= N:
    print(0)
    exit()
for i in range(K-1):
    interval.pop()
    

print(sum(interval))