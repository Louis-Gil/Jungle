import sys
from bisect import bisect_left
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0]

for case in lst:
    if dp[-1] < case:
        dp.append(case)
    else:
        dp[bisect_left(dp, case)] = case
print(len(dp)-1)