# 합격, 시간초과, 메모리초과
import sys
# sys.stdin = open('01\input.txt', 'r')

Num = int(input())
lst = [None] * Num
for i in range(Num):
    lst[i] = int((sys.stdin.readline()))
# print(Num, lst)

def shaker(Num, lst):
    left = 0
    right = Num-1
    last = right
    while left < right :
        for i in range(right, left, -1):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                last = i
            # print(lst)
        left = last
        # print("left", left)
        
        for i in range(left, right):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                last = i
            # print(lst)
        right = last
        # print("right", right)
    return lst

result = shaker(Num,lst)
# print("------------")
print(*result, sep="\n")