from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

def solution(arr, s):
    cnt = 0

    all_sum = []
    for i in range(1, len(arr) + 1):
        for i in map(sum, combinations(arr, i)):
            if i == s:
                cnt += 1

    return cnt

cnt2 = 0
def solution2(arr, s, sum_):
    global cnt2

    if sum_ and sum(sum_) == s:
        cnt2 += 1

    for i, v in enumerate(arr):
        temp = arr[i+1:]
        solution2(arr[i+1:], s, sum_ + [v])


print(solution(arr, s))

