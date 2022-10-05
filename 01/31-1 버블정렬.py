# 합격, 시간초과, 메모리초과
import sys
# sys.stdin = open('01\input.txt', 'r')

Num = int(input())
lst = [None] * Num
for i in range(Num):
    lst[i] = int((sys.stdin.readline()))
# print(Num, lst)

def bubble(Num, lst):
    for i in range(Num - 1):
        for j in range(Num - 1, i, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst

result = bubble(Num,lst)
print(*result, sep="\n")

