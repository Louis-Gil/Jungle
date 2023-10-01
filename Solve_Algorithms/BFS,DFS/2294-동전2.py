# https://www.acmicpc.net/problem/2294
import sys
from collections import deque
input = sys.stdin.readline

coin, target = map(int, input().split())
arr = set([int(input()) for _ in range(coin)])
arr = sorted(list(arr), reverse=True)
visited = [0] * (target + 1)

def bfs():
    queue = deque()
    for i in range(len(arr)):
        if arr[i] < target:
            queue.append([arr[i], arr[i], 1]) # 동전, 합, 개수
            visited[arr[i]] = 1
    while queue:
        coin, sum, count = queue.popleft()
        if sum == target:
            return count
        for i in arr:
            if coin >= i and sum + i <= target and visited[sum + i] == 0:
                queue.append([i, sum + i, count + 1])
                visited[sum + i] = 1
    return -1

print(bfs())