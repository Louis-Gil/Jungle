import sys
sys.stdin = open('01\input.txt', 'r')

num, row, col = map(int, sys.stdin.readline().split())
# print(num, row, col)

def quadrant(num, row, col, visit):
    while num != 0:
        num -= 1
        size = 2**num

        # 1사분면
        if (row < size) & (col < size):
            visit += 0

        # 2사분면
        elif (row < size) & (col >= size):
            visit += size * size
            col -= size

        # 3사분면
        elif (row >= size) & (col < size):
            visit += size * size * 2
            row -= size

        # 4사분면
        else :
            visit += size * size * 3
            row -= size
            col -= size
    return visit

visit = 0
print(quadrant(num, row, col, visit))
