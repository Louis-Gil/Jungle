import sys

# sys.stdin = open('01\input.txt', 'r')
a = int(sys.stdin.readline())

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else : return 1

print(factorial(a))