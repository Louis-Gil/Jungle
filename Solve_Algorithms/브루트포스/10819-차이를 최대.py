# https://www.acmicpc.net/problem/10819
import sys
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

permu = list(permutations(arr, n))
# print(permu)

def calculator(li):
    total = 0
    for i in range(len(li)-1):
        total += abs(li[i]-li[i+1])
    return total

answer = 0
for li in permu:
    answer = max(answer, calculator(li))

print(answer)