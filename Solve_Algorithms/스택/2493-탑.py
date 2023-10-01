# https://www.acmicpc.net/problem/2493
import sys
building_num = int(sys.stdin.readline())
building_lst = list(map(int, sys.stdin.readline().split()))
temp = 0

stack1 = []
answer = []
for i in range(building_num):
    while stack1:
        if stack1[-1][1] > building_lst[i]:
            answer.append(stack1[-1][0] + 1)
            break
        else :
            stack1.pop()
    if not stack1:
        answer.append(0)
    stack1.append([i, building_lst[i]])
print(" ".join(map(str, answer)))
