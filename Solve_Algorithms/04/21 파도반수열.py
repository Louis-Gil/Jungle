import sys
input = sys.stdin.readline

test = int(input())
num_lst = []
for i in range(test):
    num_lst.append(int(input()))

dp = [[] for _ in range(101)]
dp[1],dp[2],dp[3],dp[4],dp[5] =1,1,1,2,2

def pado(num):
    if dp[num]:
        return dp[num]
    dp[num] = pado(num-1) + pado(num-5)
    return dp[num]

for i in num_lst:
    print(pado(i))