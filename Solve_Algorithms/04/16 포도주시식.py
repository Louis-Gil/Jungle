import sys
input = sys.stdin.readline

wine_num = int(input())
wine_lst = []
for i in range(wine_num):
    wine_lst.append(int(input()))

# print(wine_num, wine_lst)

dp = [[0,0,0] for _ in range(wine_num+1)]
for i in range(1, wine_num+1):
    dp[i][0] = max(dp[i-1]) # 한턴 쉼
    dp[i][1] = dp[i-1][0] + wine_lst[i-1]
    dp[i][2] = dp[i-1][1] + wine_lst[i-1]
print(max(dp[wine_num]))
