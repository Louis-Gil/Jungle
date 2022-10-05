from collections import deque
import sys
# sys.stdin = open('02\input.txt', 'r')
word_num, kill = list(map(int, sys.stdin.readline().split()))

lst_deque = deque([i for i in range(1, word_num+1)])
TMP = "<"

for i in range(word_num):
    lst_deque.rotate((kill-1)*-1)
    TMP += f"{lst_deque.popleft()}, "

TMP = TMP[:-2] + ">"
print(TMP)