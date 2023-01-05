# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline

have = int(input())
having_cards = set(map(int, input().split()))
check = int(input())
checking_cards = list(map(int, input().split()))

# 이진탐색 # 사용안함
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

def findnum(having, checking):
    for i in checking:
        if i in having:
            print(1, end=' ')
        else:
            print(0, end=' ')

findnum(having_cards, checking_cards)