import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for x in range(n)]

result = []
def solution(n, c):
    if n == 0:
        result.append(c)
        return

    else:
        for i in range(1, 4):
            if n >= i:
                solution(n - i, c + [i])

for i in arr:
    solution(i, [])
    print(len(result))
    result = []