# https://www.acmicpc.net/problem/11816
input = input()
# print(input)

if(input[0]=='0'):
    if(input[1]=='x'):
        input = int(input, 16)
    else:
        input = int(input, 8)
print(input)