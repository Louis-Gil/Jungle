# https://www.acmicpc.net/problem/6603
import sys

def combinations(arr, r):
    result = []
    if r == 0:
        return [[]]
    for i in range(0, len(arr)):
        for next in combinations(arr[i+1:], r-1):
            result.append([arr[i]] + next)
    return result
                
while(True):
    Num = list(map(int, sys.stdin.readline().split()))
    if Num[0] == 0:
        break
    result = combinations(Num[1:], 6)
    for i in result:
        print(*i)
    print()