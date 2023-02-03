# https://www.acmicpc.net/problem/11866
from collections import deque
N, K = map(int, input().split())

deque1 = deque([i for i in range(1, N+1)])
print(deque1)

while len(deque1) > 1:
    deque1.rotate(K*(-1))
    print(deque1.popleft(), end=", ")
print(deque1.popleft(), end=">")
