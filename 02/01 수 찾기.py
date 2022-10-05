# 이진탐색으로 변환
import sys
sys.stdin = open('02\input.txt', 'r')

A = int(sys.stdin.readline())
lst1 = sorted(map(int, sys.stdin.readline().split()))
B = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))
# print(A, lst1, B, lst2)

def tree_2(lst1, i, start, end):
    if start > end:
        return 0
    pin = (start + end)//2
    if i == lst1[pin]:
        return 1
    elif i > lst1[pin]:
        return tree_2(lst1, i, pin+1, end)
    else :
        return tree_2(lst1, i, start, pin-1)

for i in lst2:
    start = 0
    end = A-1
    print(tree_2(lst1, i, start, end))

for l in lst2:
    sys.stdout.write('1 ') if l in lst1 else sys.stdout.write('0 ')
    




















# import sys
# # sys.stdin = open('02\input.txt', 'r')

# A = int(sys.stdin.readline())
# lst1 = sorted(map(int, sys.stdin.readline().split()))
# B = int(sys.stdin.readline())
# lst2 = list(map(int, sys.stdin.readline().split()))
# result = []
# # print(A, lst1, B, lst2)

# def binary(i, lst1, start, end):
#     if start > end:
#         return 0
#     B = (start+end) // 2
#     if i == lst1[B]:
#         return 1
#     elif i < lst1[B]:
#         return binary(i, lst1, start, B-1)
#     else:
#         return binary(i, lst1, B+1, end)

# for i in lst2:
#     start = 0
#     end = len(lst1)-1
#     print(binary(i, lst1, start, end))