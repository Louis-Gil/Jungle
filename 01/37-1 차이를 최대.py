import sys
from itertools import permutations
# sys.stdin = open('01\input.txt', 'r')


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