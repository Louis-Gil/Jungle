import sys
# sys.stdin = open('02\input.txt', 'r')

line_num, square = list(map(int, sys.stdin.readline().split()))
lst = []
for i in range(line_num):
    lst.append(list(map(int, sys.stdin.readline().split())))
# print(line_num, square, lst)

def gob(lst, lst2):
    num = len(lst)
    newlst = [0]*num
    for i in range(num):
        newlst[i] = [0]*num
        for j in range(num):
            for k in range(num):
                # print(lst[i][j],lst[i][k],lst[k][j])
                newlst[i][j] += (lst[i][k] * lst2[k][j])%1000
    return newlst

def solution(lst, square):
    if square == 1:
        return lst

    else :
        temp = solution(lst, square//2)
        if square % 2 == 0:
            return gob(temp, temp)
        else :
            return gob(gob(temp, temp),lst)

result = solution(lst, square)
for i in result:
    for j in i:
        print(j%1000, end=" ")
    print("")