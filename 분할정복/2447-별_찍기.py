# https://www.acmicpc.net/problem/2447
import sys

input = sys.stdin.readline
number = int(input())

def bunhal(n):
    if n==1:
        return ['*']
    
    stars = bunhal(n//3)
    list = []
    
    for i in stars:
        list.append(i*3)
    for i in stars:
        list.append(i+' '*(n//3)+i)
    for i in stars:
        list.append(i*3)
    return list

arr = bunhal(number)
print ('\n'.join(arr))
        