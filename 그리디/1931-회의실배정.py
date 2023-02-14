# # https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline
n = int(input())

room_li = []
for i in range(n):
    room_li.append(list(map(int, input().split())))

room_li.sort(key = lambda x: x[0])
room_li.sort(key = lambda x: x[1])

cnt = 1
end = room_li[0][1]

for i in range(1, n):
    if room_li[i][0] >= end:
        cnt += 1
        end = room_li[i][1]

print(cnt)