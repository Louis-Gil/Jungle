from collections import deque
import sys
# sys.stdin = open('02\input.txt', 'r')
word_num = int(sys.stdin.readline())
result_queue = deque()
lst = []
# for i in range(word_num):
#     lst.append(sys.stdin.readline().split())

for _ in range(word_num):
    lunch = sys.stdin.readline().split()
    if lunch[0] == 'push':
        result_queue.append(lunch[1])
    elif lunch[0] == 'pop':
        if not result_queue :
            print('-1')
        else:
            temp = result_queue.popleft()
            print(temp)
    elif lunch[0] == 'size':
        print(len(result_queue))
    elif lunch[0] == 'empty':
        if not result_queue :
            print('1')
        else :
            print('0')
    elif lunch[0] == 'front':
        if not result_queue:
            print('-1')
        else:
            print(result_queue[0])
    else : # back
        if not result_queue:
            print('-1')
        else:
            print(result_queue[-1])