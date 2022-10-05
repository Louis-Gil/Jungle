import sys
# sys.stdin = open('02\input.txt', 'r')

X, Y, Z = list(map(int, sys.stdin.readline().split()))
answer = []
# print(X, Y, Z)

def gob(X, Y):
    if Y == 1:
        return X % Z
    else : 
        temp = gob(X, Y//2)
        if Y % 2 == 0:
            return temp * temp % Z
        else :
            return temp * temp * X % Z

result = gob(X, Y)
print(result)