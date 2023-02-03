# https://www.acmicpc.net/problem/2164
from collections import deque
import sys

list_deque = deque()
num = int(input())
list_deque.extend([i for i in range(1, num+1)])
print(list_deque)

for i in range(num-1):
    list_deque.popleft()
    list_deque.rotate(-1)
print(*list_deque)