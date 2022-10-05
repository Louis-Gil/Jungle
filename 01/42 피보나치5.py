import sys

# sys.stdin = open('01\input.txt', 'r')
a = int(sys.stdin.readline())


def fibonachi(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else :
        return fibonachi(num-1) + fibonachi(num-2)

if a == 0:
    print(0)
else :
    print(fibonachi(a))