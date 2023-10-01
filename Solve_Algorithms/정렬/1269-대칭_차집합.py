# https://www.acmicpc.net/problem/1269
import sys

A_count, B_count = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


array1 = set(A)-set(B)
array2 = set(B)-set(A)
print(len(array1)+len(array2))