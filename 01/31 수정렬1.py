import sys
# sys.stdin = open('01\input.txt', 'r')

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
# print(list)


def fix_list(list, num):
    for i in range(num-1):
        for k in range(num-1):
            if list[k] > list[k+1]: list[k],list[k+1]=list[k+1],list[k]

fix_list(list, n)
for i in range(n):
    print(list[i]) 