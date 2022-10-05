import sys
sys.stdin = open('02\input.txt', 'r')

circle_num = int(sys.stdin.readline())
circle_lst =[]
for i in range(circle_num):
    A, B = list(map(int, sys.stdin.readline().split()))
    A, B = A - B, A + B
    circle_lst.append([A, B])
circle_lst.sort()
# print(circle_lst, circle_lst[0][0])

result = 1
result_lst = set()
for i in range(circle_num):
    result_lst.add(circle_lst[i][0])
    if circle_lst[i][1] in result_lst:
        result += 1
    result_lst.add(circle_lst[i][1])
    result += 1
print(result)
