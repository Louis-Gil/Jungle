# https://www.acmicpc.net/problem/2630
import sys

line_num = int(sys.stdin.readline())
paper = []
for _ in range(line_num):
    paper.append(list(map(int, sys.stdin.readline().split())))
result = []

def paper_cut(x,y,N):
    color=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color!=paper[i][j]:
                paper_cut(x,y,N//2)
                paper_cut(x,y+N//2,N//2)
                paper_cut(x+N//2,y,N//2)
                paper_cut(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        result.append(0)
    else :
        result.append(1)
paper_cut(0,0,line_num)
print(result.count(0))
print(result.count(1))