# 분할정복 다시 확인할것

import sys
input = sys.stdin.readline

def solution(mx, my, length, area):
    global tile_num
    
    if length <= 1:
        count = 3
        if area == 0 or area == 4:
            for i in range(mx, mx+2):
                for j in range(my, my+2):
                    if not board[i][j] and count :
                        board[i][j] = tile_num
                        count -= 1
        
        elif area == 1:
            for i in range(mx, mx+2):
                for j in range(my+1, my-1, -1):
                    if not board[i][j] and count :
                        board[i][j] = tile_num
                        count -= 1
        
        elif area == 2:
            for i in range(mx+1, mx-1, -1):
                for j in range(my, my+2):
                    if not board[i][j] and count:
                        board[i][j] = tile_num
                        count -= 1
            
        else :
            for i in range(mx+1, mx-1, -1):
                for j in range(my+1, my-1, -1):
                    if not board[i][j] and count:
                        board[i][j] = tile_num
                        count -= 1
            
        tile_num += 1
        return

    solution(mx, my, length-1, 0)
    solution(mx, my+2**(length-1), length-1, 1)
    solution(mx + 2**(length-1), my, length-1, 2)
    solution(mx + 2**(length-1), my+2**(length-1), length-1, 3)
    solution(mx + 2**length//4, my + 2**length//4, length-1, 4)
    
        

length = int(input())
x, y = map(int, input().split())
print(length, x, y)

board = [[0] * (2**length) for _ in range(2**length)]
board[2**length - y][x - 1] = -1
print(board)

tile_num = 1
solution(0,0,length,0)

for row in board:
    for col in row:
        print(col, end=' ')
    print( )
