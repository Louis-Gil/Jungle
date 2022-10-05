import sys

n, row, col = map(int, sys.stdin.readline().split())

visit = 0
while n != 0:
    n -= 1
    size = 2 ** n

    # 1사분면
    if row < size and col < size:
        visit += 0

    # 2사분면
    elif row < size and col >= size:
        visit += size * size
        col -= size

    # 3사분면
    elif row >= size and col < size:
        visit += size * size * 2
        row -= size

    # 4사분면
    else:
        visit += size * size * 3
        row -= size
        col -= size

print(visit)