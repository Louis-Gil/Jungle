from collections import deque
import sys

field_num = int(sys.stdin.readline())
apple_num = int(sys.stdin.readline())
apple_lst = []
for _ in range(apple_num):
    apple_lst.append(list(map(int, sys.stdin.readline().split())))
turn_lst = deque()
turn_num = int(sys.stdin.readline())
for _ in range(turn_num):
    turn_lst.append(list(sys.stdin.readline().split()))
# print(field_num, apple_lst, turn_lst)

current = [1, 1]
turn_total = deque([1,2,3,4])
turn_dic = 0
bam_queue = deque([0])
day = 0

while (0 < current[0] < field_num+1) & (0 < current[1] < field_num+1) & (current not in bam_queue):
    day += 1
    bam_queue.append(current[:]) #나이 많아지면 커짐

    if turn_total[turn_dic] == 1:
        current[1] += 1
    elif turn_total[turn_dic] == 2:
        current[0] += 1
    elif turn_total[turn_dic] == 3:
        current[1] -= 1
    else : #4
        current[0] -= 1

    if current not in apple_lst:
        bam_queue.popleft()
    else : 
        apple_lst.remove(current)
        # print('먹었당')

    if turn_lst:
        if (turn_lst[0][0] == str(day)):
            if turn_lst[0][1] == 'L':
                turn_total.rotate(1)
            else:
                turn_total.rotate(-1)
            turn_lst.popleft()
            # print('돌았당')
    # print('살았당 현재위치', current, bam_queue, day)
print(day)
