# https://www.acmicpc.net/problem/2231
import sys
number = sys.stdin.readline().strip()

def solution(number):
    for i in range(1, int(number)):
        if i + sum(map(int, str(i))) == int(number):
            print(i)
            break
        if i == int(number) - 1:
            print('0')

if number == '1':
    print(0)
else :
    solution(number)