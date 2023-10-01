# https://www.acmicpc.net/problem/2504
import sys
word = sys.stdin.readline().rstrip()

stack1 = []
tmp = 1
res = 0
for i in range(len(word)):
    if word[i] == '(':
        tmp *= 2
        stack1.append(word[i])
    elif word[i] == '[':
        tmp *= 3
        stack1.append(word[i])
    elif word[i] == ')':
        if not stack1 or stack1[-1] == '[':
            res = 0
            break
        if word[i-1] == '(':
            res += tmp
        tmp //= 2
        stack1.pop()
    else :
        if not stack1 or stack1[-1] == '(':
            res = 0
            break
        if word[i-1] == '[':
            res += tmp
        tmp //= 3
        stack1.pop()
if stack1:
    res = 0
print(res)