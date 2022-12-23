# https://www.acmicpc.net/problem/8595
num = int(input())
input = input()
# print(num, input)

temp = ''
result = 0

for i in input:
    if i.isdigit() :
        temp += i
    elif temp :
        # temp에 넣은 숫자들 합을 result로 넣어줌
        result += int(''.join(temp))
        temp = []

if temp :
# 위와 동일
    result += int(''.join(temp))
    

print(result)