# https://www.acmicpc.net/problem/2098
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(1 << N)] for _ in range(N)]
def recursion(cur, visited):
    if visited == (1 << N) - 1:
        if board[cur][0] == 0:
            return 9876543210
        dp[cur][visited] = board[cur][0]
        return board[cur][0]
    
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    min_dist = 9876543210
    for i in range(N):
        if not visited & (1 << i) and board[cur][i] != 0:
            min_dist = min(min_dist, board[cur][i] + recursion(i, visited | (1 << i)))
    dp[cur][visited] = min_dist
    return min_dist
print(recursion(0, 1))