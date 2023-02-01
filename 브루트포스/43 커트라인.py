import sys

# sys.stdin = open('01\input.txt', 'r')
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
b.sort(reverse=True)

print(b[a[1]-1])