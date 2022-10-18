# N = int(input())
# time = []

# for _ in range(N):
#   start, end = map(int, input().split())
#   time.append([start, end])

# time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
# time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
# # print(time)

# last = 0 # 회의의 마지막 시간을 저장할 변수
# conut = 0 # 회의 개수를 저장할 변수

# for i, j in time:
#   if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
#     conut += 1
#     last = j

# print(conut)

import sys

input = sys.stdin.readline
n = int(input())

room_li = []
for i in range(n):
    room_li.append(list(map(int, input().split())))

room_li.sort(key = lambda x: x[0])
# 일단 시작점을 1에 근접한 값들로 설정을 한다

room_li.sort(key = lambda x: x[1])
# 시작점이 오른 차순을 시작으로 end값에 따라 end값이 기달면 배열을 뒤로
# 밀어 버린다.   이렇게 되면 나중에 end값만 보면 최대 회의의 개수를 알 수 있게된다.

cnt = 1
end = room_li[0][1]

for i in range(1, n):
    if room_li[i][0] >= end:
        cnt += 1
        end = room_li[i][1]

print(cnt)