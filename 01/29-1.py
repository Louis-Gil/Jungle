import sys
sys.stdin = open('01\input.txt', 'r')

n = int(sys.stdin.readline())

flag1 = [False] * n

pos = [0] * n

def put(n):
    for i in range(n):
        print(f'{pos[i]:2}', end='')
    print()

def set(i, n) :
    for j in range(n):
        if flag1[j] == False:
            pos[i] = j
            if i == (n-1):
                put(n)
            else :
                flag1[j] = True
                set(i+1, n)

set(0, n)