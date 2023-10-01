# https://www.acmicpc.net/problem/11720
count = int(input())
number = input()
result = 0

for i in number:
    result += int(i)
    
print(result)