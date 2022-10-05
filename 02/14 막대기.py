import sys
from collections import deque
sys.stdin = open('02\input.txt', 'r')

wood_num = int(sys.stdin.readline())
wood_lst = deque()
for i in range(wood_num):
    wood_lst.append(int(sys.stdin.readline()))


height = 0
count = 0
for i in wood_lst[::-1]:
    if height < i:
        height = i
        count += 1
    else :
        continue
print(count)
