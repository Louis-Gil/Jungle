import sys
input = sys.stdin.readline

num = int(input())
num_lst = []
for i in range(num):
    num_lst.append(list(map(int, input().split())))
# print(num, num_lst)

def rgb(color):
    DP = [[0]*3 for _ in range(num+1)]

    DP[1] = [1e9, 1e9, 1e9]
    DP[1][color] = num_lst[0][color]

    for i in range(2, num+1):
        for j in range(3):
            DP[i][j] = min(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3]) + num_lst[i-1][j]

    little_result = min(DP[-1])
    return little_result

result = 1e9
for i in range(3):
    result = min(rgb(i), result)
print(result)