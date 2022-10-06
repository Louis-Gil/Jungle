import sys
# sys.stdin = open('test\\02\input.txt', 'r')

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

bomb_lastChar = str2[-1]
stack = []
bomb_length = len(str2)

for char in str1:
    stack.append(char)
    if char == bomb_lastChar and ''.join(stack[-bomb_length:])==str2:
        del stack[-bomb_length:]

# while True:
#     str1 = str1.replace(str2, "")
#     if str2 not in str1:
#         break

# stack1 = []
# for i in range(len(str1)):
#     if 

# if str1:
#     print(str1)
# else:
#     print("FRULA")

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
    