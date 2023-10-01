# https://www.acmicpc.net/problem/1654
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)
result = 0
while(start<=end):
    mid = (start + end) // 2
    cnt = 0

    for i in arr:
        cnt += i // mid
    if(cnt >= m):
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    
print(result)