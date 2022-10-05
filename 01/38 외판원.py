import sys
from itertools import permutations
sys.stdin = open('01\input.txt', 'r')

n = int(input())
Get_list = []
for i in range(n):
    Get_list.append(list(map(int, input().split())))
# print(n, Get_list)

result = 0
route = list(permutations(list(range(n))))
# print(route[0])
# print(Get_list[0][1])

for i in route:
    sum = 0
    for j in range(n):
        num = Get_list[i[j]][i[(j+1)%n]]
        if num == 0:
            break
        sum += num
    if result == 0:
        result = sum
    elif result > sum:
        result = 0

print(result)