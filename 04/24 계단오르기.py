import sys
input = sys.stdin.readline

num = int(input())
stair_lst = []
for i in range(num):
    stair_lst.append(int(input()))
# print(num, stair_lst)

dp = [[0]*3 for _ in range(num+1)]
# print(dp)
dp[1][1] = stair_lst[0]
for i in range(2, num+1):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i-1][0]+stair_lst[i-1]
    dp[i][2] = dp[i-1][1]+stair_lst[i-1]

print(max(dp[-1][1], dp[-1][2]))