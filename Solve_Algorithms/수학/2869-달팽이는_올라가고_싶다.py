# https://www.acmicpc.net/problem/2869
import sys
import math
a = list(map(int, sys.stdin.readline().split()))
work = math.ceil((a[2]-a[0])/(a[0]-a[1]))
print(work+1)