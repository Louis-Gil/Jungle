# https://www.acmicpc.net/problem/9012
import sys

word_num = int(sys.stdin.readline())
word_lst = []
for i in range(word_num):
    word_lst.append((sys.stdin.readline().rstrip()))
# print(word_lst)
stack1 = []
stack2 = []

for i in word_lst:
    stack1 = []
    stack2 = []
    for j in i:
        if j == '(':
            stack1.append(1)
        elif (j == ')') & (len(stack1) > 0):
            stack1.pop()
        else:
            stack2.append("NO")
            break
    if (not stack1):
        stack2.append("YES")
    elif (len(stack1) > 0):
        stack2.append("NO")
    print(stack2[0])