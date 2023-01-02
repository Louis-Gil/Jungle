# https://www.acmicpc.net/problem/10974
# 순열
import sys

Num = int(sys.stdin.readline())

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i] + arr[i+1:], r - 1):
                yield [arr[i]] + next

result = list(permutation([i for i in range(1, Num + 1)], Num))
for i in result:
    print(*i)
