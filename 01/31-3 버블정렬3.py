# 합격, 시간초과, 메모리초과
import sys
sys.stdin = open('01\input.txt', 'r')

Num = int(input())
lst = [None] * Num
for i in range(Num):
    lst[i] = int((sys.stdin.readline()))
# print(Num, lst)

def bubble(Num, lst):
    k = 0
    while k < Num-1 :
        last = Num-1
        exchange = 0
        for i in range(Num-1, k, -1):
            print(lst)
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                last = i
                exchange += 1
        if exchange == 0 : break
        k = last

    return lst

result = bubble(Num,lst)
print("------------")
print(*result, sep="\n")

# 7
# 6
# 4
# 3
# 7
# 1
# 9
# 8
