import sys
sys.stdin.readline

number = int(input())
lec_lst = []
for i in range(number):
    lec_lst.append(list(map(int, input().split())))

lec_lst.sort()
dp = [1]*number

for i in range(number):
    for j in range(i):
        if lec_lst[i][1] > lec_lst[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(number-max(dp))