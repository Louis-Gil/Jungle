import sys
input = sys.stdin.readline
 
# 초기 입력
N = int(input()) # 추의 갯수
wgt = list(map(int, input().split())) # 추
M = int(input()) # 구슬의 갯수
mbl = list(map(int, input().split())) # 구슬

s = set()
for i in wgt:
    temp_set = set()
    for j in s:
        temp_set.add(i + j)
        temp_set.add(abs(i - j))
    temp_set.add(i)
    s |= temp_set

for i in mbl:
    print("Y" if i in s else "N", end = ' ')
print()