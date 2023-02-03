# https://www.acmicpc.net/problem/3190
from collections import deque
import sys
input = sys.stdin.readline

board_size = int(input())
apple_count = int(input())
apple_locations = []
for _ in range(apple_count):
    apple_locations.append(list(map(int, input().split())))
turn_count = int(input())
turn_commands = deque()
for _ in range(turn_count):
    turn_commands.append(list(input().split()))
# print(board_size, apple_locations, turn_commands)

day = 0
snake_head = [1, 1]
snake_body = deque([[1, 1]])
snake_direction = deque([0, 1, 2, 3]) #오른쪽, 아래, 왼쪽, 위

while True:
    # 시간 설정
    day += 1
    
    # 머리 이동
    if snake_direction[0] == 0:
        snake_head = [snake_body[-1][0], snake_body[-1][1] + 1]
    elif snake_direction[0] == 1:
        snake_head = [snake_body[-1][0] + 1, snake_body[-1][1]]
    elif snake_direction[0] == 2:
        snake_head = [snake_body[-1][0], snake_body[-1][1] - 1]
    elif snake_direction[0] == 3:
        snake_head = [snake_body[-1][0] - 1, snake_body[-1][1]]
    
    # 머리가 몸에 닿거나 벽에 닿으면 종료
    if (snake_head in snake_body) or (snake_head[0] < 1) or (snake_head[0] > board_size) or (snake_head[1] < 1) or (snake_head[1] > board_size):
        break
    
    # 사과 처리
    if (snake_head in apple_locations):
        snake_body.append(snake_head)
        apple_locations.remove(snake_head)
    else:
        snake_body.append(snake_head)
        snake_body.popleft()
    
    # 방향 지시
    if turn_commands and (int(turn_commands[0][0]) == day):
        if turn_commands[0][1] == 'L':
            snake_direction.rotate(1)
        else:
            snake_direction.rotate(-1)
        turn_commands.popleft()

print(day)