import sys
from itertools import permutations
# sys.stdin = open('01\input.txt', 'r')

A = int(sys.stdin.readline())
# print(A)

for i in range(A):
    B=i
    for j in str(i):
        B += int(j)
    if B == A:
        print(i)
        break
    if i == (A-1):
        print('0')