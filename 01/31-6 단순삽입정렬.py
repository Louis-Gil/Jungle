# 합격, 시간초과, 메모리초과
import sys
sys.stdin = open('01\input.txt', 'r')

Num = int(input())
lst = [None] * Num
for i in range(Num):
    lst[i] = int((sys.stdin.readline()))

def insertion(Num,lst):
    for i in range(1,Num):
        j = i
        tmp = lst[i]
        while j > 0 and lst[j-1] > tmp:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmp
    return lst



result = insertion(Num,lst)
# print("------------")
print(*result, sep="\n")