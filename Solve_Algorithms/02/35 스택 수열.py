import sys
from collections import deque
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
lst = deque()
for i in range(num):
    lst.append(int(sys.stdin.readline()))

result = []
stack1 = deque()
for i in range(1, num+1):
    stack1.append(i)
    result.append("+")
    while stack1 and (stack1[-1] == lst[0]):
        lst.popleft()
        stack1.pop()
        result.append("-")
if stack1:
    print("NO")
else :
    print(*result, sep="\n")