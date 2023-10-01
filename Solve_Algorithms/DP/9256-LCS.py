# https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

l1 = len(word1)
l2 = len(word2)

dp = [[0] * (l2+1) for _ in range(l1+1)]

def dp_LCS():
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
print(dp_LCS())

