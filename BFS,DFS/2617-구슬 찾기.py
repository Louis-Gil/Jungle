# https://www.acmicpc.net/problem/2617
"""_summary_
중간 무게는 (N+1)//2 번째
dfs로 가벼운 구슬을 구한다
bfs로 무거운 구슬을 구한다
"""
import sys
from collections import deque
input = sys.stdin.readline

marble_num, line_num = map(int, input().split())
light_lst = [[] for _ in range(marble_num+1)]
heavy_lst = [[] for _ in range(marble_num+1)]
mid = (marble_num+1)//2
for i in range(line_num):
    A, B = map(int, input().split())
    light_lst[B].append(A)
    heavy_lst[A].append(B)

def dfs(arr, n):
    global cnt1
    visited1[n] = True
    for i in arr[n]:
        if not visited1[i]:
            visited1[i] = True
            cnt1 += 1
            dfs(arr, i)
            
def bfs(arr, n):
    global cnt2
    queue = deque([n])
    visited2[n] = True
    while queue:
        node = queue.popleft()
        for i in arr[node]:
            if not visited2[i]:
                visited2[i] = True
                cnt2 += 1
                queue.append(i)
                

result = 0

for i in range(1, marble_num+1):
    cnt1 = 0
    cnt2 = 0
    visited1 = [False]*(marble_num+1)
    dfs(light_lst, i)
    if cnt1 >= mid:
        result+=1
        continue
    
    visited2 = [False]*(marble_num+1)
    bfs(heavy_lst, i)
    if cnt2 >= mid:
        result+=1
        continue
print(result)