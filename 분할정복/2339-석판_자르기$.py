# https://www.acmicpc.net/problem/2339
import sys

input = sys.stdin.readline
number = int(input())

arr = []
for i in range(number):
    arr.append(list(map(int,input().split())))

def cutting(startX, endX, startY, endY, board, direction):
    star = 0
    broken = 0
    
    for i in range(startX, endX):
        for j in range(startY, endY):
            if arr[i][j] == 2:
                star += 1
            elif arr[i][j] == 1:
                broken += 1
    
    if(star==1 and broken==0):
        return 1
    elif(star==1 and broken==1):
        return 0
    elif(star==0):
        return 0
    elif(star>2 and broken==0):
        return 0
    
    answer = 0
    
    for i in range(startX, endX):
        for j in range(startY, endY):
            if i == startX or i == endX or j == startY or j == endY:
                continue
            if(board[i][j] == 1):
                if(direction != 0):
                    answer += cutting(startX, i, startY, endY, board, 0) * cutting(i+1, endX, startY, endY, board, 0)
                else:
                    answer += cutting(startX, endX, startY, j, board, 1) * cutting(startX, endX, j+1, endY, board, 1)    
    return answer

result = cutting(0, number, 0, number, arr, 0) + cutting(0, number, 0, number, arr, 1)
print( cutting(0, number, 0, number, arr, 0) )
print( cutting(0, number, 0, number, arr, 1) )
if(result == 0):
    print(-1)
else:
    print(result)
