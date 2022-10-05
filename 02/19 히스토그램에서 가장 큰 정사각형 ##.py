from collections import deque
import sys
sys.stdin = open('02\input.txt', 'r')
while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)
    print(rec)
    if n == 0:
        break
    stack = deque()
    answer = 0

    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            tmp = stack.pop()
            if len(stack) == 0:
                width = i
            else :
                width = i - stack[-1] -1
            answer = max(answer, width * rec[tmp])
        stack.append(i)

    while len(stack) != 0 :
        tmp= stack.pop()

        if len(stack) == 0:
            width = n
        else :
            width = n - stack[-1] -1
        answer = max(answer, width * rec[tmp])
        
    print(answer)