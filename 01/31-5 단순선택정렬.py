# 합격, 시간초과, 메모리초과
import sys
# sys.stdin = open('01\input.txt', 'r')

Num = int(input())
lst = [None] * Num
for i in range(Num):
    lst[i] = int((sys.stdin.readline()))
# print(Num, lst)

def selection(Num,lst):
    for i in range(Num-1):
        min = i
        for j in range(i+1, Num):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst



result = selection(Num,lst)
# print("------------")
print(*result, sep="\n")