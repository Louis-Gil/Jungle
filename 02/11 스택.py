import sys
# sys.stdin = open('02\input.txt', 'r')

word_num = int(sys.stdin.readline())
word_lst = []
for i in range(word_num):
    word_lst.append(list(map(str, sys.stdin.readline().split())))
# print(word_num, word_lst)

stack1 = []

for i in word_lst:
    if i[0] == 'push':
        stack1.append(i[1])
    elif i[0] == 'pop':
        if not stack1:
            print('-1')
        else : 
            temp = stack1.pop()
            print(temp)
    elif i[0] == 'size':
        print(len(stack1))
    elif i[0] == 'empty':
        if not stack1:
            print('1')
        else :
            print('0')
    else: #top
        if not stack1:
            print(-1)
        else :
            print(stack1[-1])