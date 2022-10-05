import sys
sys.stdin = open('01\input.txt', 'r')
num1 = int(input())
pick = int(input())

card = []

for _ in range(num1):
    card.append(int(input()))


dp = [0] * num1
string = ''
result = set()


def select(cnt):
    global string

    if cnt == pick:
        result.add(string)
        print(dp)
        return

    for i in range(num1):
        if dp[i] == 0:
            dp[i] = 1

            tmp = str(card[i])
            string += tmp

            select(cnt + 1)

            dp[i] = 0
            string = string[:-len(tmp)]


select(0)
print(result)
print(len(result))