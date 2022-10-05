from collections import deque
import sys
# sys.stdin = open('02\input.txt', 'r')
# word_num = int(sys.stdin.readline())

# lst_deque = deque()
# for i in range(word_num):
#     lst_deque.append(i+1)
# # print(word_num, lst_deque)
lst_deque = deque([i for i in range(1, int(input())+1)])

for i in range(len(lst_deque)-1):
    lst_deque.popleft()
    lst_deque.rotate(-1)
print(*lst_deque)