# https://www.acmicpc.net/problem/2343
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

vm = max(arr)
start = vm
end = sum(arr)

res = 10**9
while(start <= end):
    mid = (start + end) // 2
    cnt = 1
    tmp = 0
    for i in range(n):
        if(tmp + arr[i] <= mid):
            tmp += arr[i]
        else:
            cnt += 1
            tmp = arr[i]
        if(cnt > m):
            break
    if(cnt > m):
        start = mid + 1
    else:
        end = mid-1
        if(mid >= vm):
            res = min(res, mid)
print(res)
