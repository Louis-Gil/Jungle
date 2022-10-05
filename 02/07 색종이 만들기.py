import sys
sys.stdin = open('02\input.txt', 'r')

line_num = int(sys.stdin.readline())
paper = []
for _ in range(line_num):
    paper.append(list(map(int, sys.stdin.readline().split())))


print(line_num, paper, paper[0][1])
result = []

def test(x,y,line_num):
    color = paper[x][y]
    for i in range(x, x+line_num):
        for j in range(y, y+line_num):
            if color != paper[i][j]:
                test(x, y, line_num//2)
                test(x, y+line_num//2, line_num//2)
                test(x+line_num//2, y, line_num//2)
                test(x+line_num//2, y+line_num//2, line_num//2)
                return
    if color == 0:
        result.append(0)
    else :
        result.append(1)


# if함수 전체 합이 라인 제곱
# 맞으면 카운트 1
# 아니면 컷
def paper_cut(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                paper_cut(x, y, N//2)
                paper_cut(x, y+N//2, N//2)
                paper_cut(x+N//2, y, N//2)
                paper_cut(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

test(0, 0, line_num)
# print(result.count(0))
# print(result.count(1))


