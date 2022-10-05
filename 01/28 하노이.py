import sys
# sys.stdin = open('01\input.txt', 'r')

n = int(sys.stdin.readline())

def hanoi(int, num1, num2):
    if n > 20:
        return

    if int != 1:
        hanoi(int-1, num1, 6-num1-num2)
        print(num1, num2)
        hanoi(int-1, 6-num1-num2, num2)

    else:
        print(num1, num2)


print(2**n - 1)
hanoi(n, 1, 3)
