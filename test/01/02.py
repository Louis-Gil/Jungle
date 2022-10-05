import sys
from itertools import product
A = int(sys.stdin.readline())
B = []
while True:
    tmp = int(sys.stdin.readline())
    if tmp < 11:
        B.append(tmp)
    if len(B) == A:
        break
C = [1,2,3]

def plus_123(num):
    if num < 3:
        D = num
    else:
        start = (num//3)
        count = 0
        for i in range(start, num-1):
            for j in product(C, repeat=i):
                if sum(j) == num:
                    # print(j)
                    count += 1
        count += num
        D = count
    print(D)


for i in B:
    plus_123(i)