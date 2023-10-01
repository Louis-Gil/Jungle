# https://www.acmicpc.net/problem/9663
# import sys
# sys.stdin = open('01\input.txt', 'r')
# n = int(sys.stdin.readline())
# n = 8

# pos = [0] * n
# flag1 = [False] * n
# flag2 = [False] * (n*2-1)
# flag3 = [False] * (n*2-1)

# def nqueen(cur, num):
#     for i in range(num):
#         if ((flag1[i] is False) & (flag2[cur + i] is False) & (flag3[cur - i + 7] is False)):
#             pos[cur] = i
#             if cur == num -1:
#                 #put()
#                 for j in range(num):
#                     print(f'{pos[j]:2}', end='')
#                 print()

#             else :
#                 flag1[i] = flag2[cur + i] = flag3[cur - i + 7] = True
#                 nqueen(cur+1, num)
#                 flag1[i] = flag2[cur + i] = flag3[cur - i + 7] = False

# nqueen(0, n)


def is_promising(x):
    for i in range(x):
        if border[x] == border[i] or abs(border[x] - border[i]) == abs(x - i):
            return False
    return True
def nqueen(x):
    global count
    if x == N:
        count += 1
        return
    else:
        for i in range(N):
            border[x] = i
            if is_promising(x):
                nqueen(x + 1)
    return count
N = 8
border = [0] * N
count = 0
print(nqueen(0))