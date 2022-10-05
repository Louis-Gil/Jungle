import sys
# sys.stdin = open('02\input.txt', 'r')

str1 = list(sys.stdin.readline().strip())
str2 = []
num = int(sys.stdin.readline())


for i in range(num):
    temp = list(map(str, sys.stdin.readline().split()))
    if temp[0] == "P":
        str1.append(temp[1])
    elif temp[0] == "L":
        if str1 : 
            str2.append(str1.pop())
    elif temp[0] == "D":
        if str2:
            str1.append(str2.pop())
    else : #B
        if str1:
            str1.pop()

print(''.join(str1 + list(reversed(str2))))



