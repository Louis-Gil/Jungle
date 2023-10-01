# https://www.acmicpc.net/problem/1654
import sys

input = sys.stdin.readline
lan_num, need_num = map(int, input().split())
lan_arr = [int(input()) for _ in range(lan_num)]

start = 1
end = max(lan_arr)
large_cm = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(lan_num):
        count += lan_arr[i]//mid
    if count >= need_num:
        start = mid + 1
        large_cm = mid
    else:
        end = mid - 1
print(large_cm)