# https://www.acmicpc.net/problem/2798
import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
Numbers = list(map(int, sys.stdin.readline().split()))

nCr = itertools.combinations(Numbers, 3)
result = 0

for i in list(nCr):
    if sum(i) <= m and sum(i) > result:
        result = sum(i)
        
print(result)