import sys
a = list(map(int, sys.stdin.readline().split()))

A = min(a[2]-a[0], a[0]-0, a[3]-a[1], a[1]-0)
print(A)