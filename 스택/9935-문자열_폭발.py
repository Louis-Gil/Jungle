# https://www.acmicpc.net/problem/9935
import sys

input = sys.stdin.readline

text_line = input().strip()
boom = input().strip()

last_char = boom[-1]
result = []

for char in text_line:
    result.append(char)
    # print(result[-len(boom):])
    if char == last_char and ''.join(result[-len(boom):]) == boom:
        del result[-len(boom):]
    
result = ''.join(result)    

if result :
    print(result)
else:
    print('FRULA')