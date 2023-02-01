# https://www.acmicpc.net/problem/2309
import sys

lst = []
for _ in range(9):
    lst.append(int(sys.stdin.readline()))


def nanjang(lst):
    lst.sort()
    for i in range(9):
        for j in range(9):
            if i != j:
                new_lst = [x for x in lst if (x != lst[i])&(x != lst[j])]
                if sum(new_lst) == 100:
                    return new_lst


result = nanjang(lst)
for i in result:
    print(i)
