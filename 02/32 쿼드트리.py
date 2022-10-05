import sys
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())
cor = []
for i in range(num):
    A = sys.stdin.readline().rstrip()
    cor.append(A)
# print(cor)

count = 0
result = []

def quad(x, y, num):
    global count
    color = cor[x][y]
    # 원소 넘기며 컬러가 아니면 재귀 while
    for i in range(y,y+num):
        for j in range(x, x+num):
            if cor[j][i] != color:
                result.append("(")
                quad(x, y, num//2)
                quad(x, y+num//2, num//2)
                quad(x+num//2, y, num//2)
                quad(x+num//2, y+num//2, num//2)
                result.append(")")
                return
    # 모두 컬러가 맞다면
    result.append(color)
    return
    # print(color)


quad(0, 0, num)
print(*result, sep="")
