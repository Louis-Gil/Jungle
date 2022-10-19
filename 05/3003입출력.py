import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))
want = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(want[i]- lst[i], end=" ")