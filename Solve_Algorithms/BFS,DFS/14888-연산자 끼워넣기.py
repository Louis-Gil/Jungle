# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

N = int(input())
N_arr=list(map(int, input().split()))
operation=list(map(int, input().split()))

max_value = -1000000000
min_value = 1000000000

def dfs(v, c):
    global max_value, min_value
    if c==N-1:
        max_value = max(max_value, v)
        min_value = min(min_value, v)
        return
    c += 1
    for i in range(4):
        if operation[i] > 0 and i==0:
            operation[i] -= 1
            dfs(v+N_arr[c], c)
            operation[i] += 1
        elif operation[i] > 0 and i==1:
            operation[i] -= 1
            dfs(v-N_arr[c], c)
            operation[i] += 1
        elif operation[i] > 0 and i==2:
            operation[i] -= 1
            dfs(v*N_arr[c], c)
            operation[i] += 1
        elif operation[i] > 0 and i==3:
            operation[i] -= 1
            dfs(int(v/N_arr[c]), c)
            operation[i] += 1
                
dfs(N_arr[0], 0)
print(max_value)
print(min_value)