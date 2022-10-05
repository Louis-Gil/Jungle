import sys
from itertools import combinations
A, Num = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# print(A, Num, B)
count = 0
for i in range(1, A+1):
    for j in combinations(B, i):
        if sum(j) == Num:
            count += 1
print(count)