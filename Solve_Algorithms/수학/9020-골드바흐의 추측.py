# https://www.acmicpc.net/problem/9020
import sys
import math
a = int(sys.stdin.readline())
b = []
for i in range(a):
    number = int(sys.stdin.readline())
    b.append(number)
maxnum = max(b)
# maxnum_fix = int(maxnum / 2) + 1

sosu = [2]
for i in range(3, maxnum, 2):
    sosu_max = max(sosu)
    for k in sosu:
        if i % k == 0:
            break
        if k == sosu_max:
            sosu.append(i)
# print(sosu)
for i in b:
    for k in range(int(i/2), 1, -1):
        num_A = k
        num_B = i - num_A
        if (num_A in sosu)&(num_B in sosu):
            print(num_A, num_B)
            break