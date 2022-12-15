import sys
input = sys.stdin.readline

# 숫자를 받는다
# 자리수 만큼 비트
# 25114 일때 11111, 11110, 11101, 10111, 10110, 10101
# dp적 요소로는 (25), (2/5) 일때 114에 대해 저장 및 재사용 등
# 비트를 나누는 기준은 26을 넘어가는지?

number = list(map(int,input().strip()))
len = len(number)
dp = [0 for _ in range(len+1)]
result = 0
print(number, len, result)

number = [0] + number
dp[0] = dp[1] = 1
print(number, dp)

for i in range(2, len+1):
    if number[i] > 0:
        dp[i] += dp[i-1]
    temp = number[i-1] * 10 + number[i]
    if temp >= 10 and temp <= 26:
        dp[i] += dp[i-2]
print(dp[len] % 1000000)