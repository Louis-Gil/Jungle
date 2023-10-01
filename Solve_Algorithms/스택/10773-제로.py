import sys

word_num = int(sys.stdin.readline())
word_lst = []
for i in range(word_num):
    word_lst.append(int(sys.stdin.readline()))
# print(word_lst)
stack1 = []

for i in word_lst:
    if i != 0:
        stack1.append(i)
    else: #0
        stack1.pop()

print(sum(stack1))