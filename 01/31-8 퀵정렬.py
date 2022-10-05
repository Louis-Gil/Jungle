from typing import MutableSequence
import sys
sys.stdin = open('01\input.txt', 'r')

def sort3(a, idx1, idx2, idx3):
    if a[idx2] < a[idx1] : a[idx2],a[idx1] = a[idx1],a[idx2]
    if a[idx3] < a[idx2] : a[idx3],a[idx2] = a[idx2],a[idx3]
    if a[idx2] < a[idx1] : a[idx2],a[idx1] = a[idx1],a[idx2]
    return idx2

def insertion_sort(a, left, right):
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1]>tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
    return a

def qsort(a : MutableSequence, left:int, right:int) -> None:
    if right - left < 9:
        insertion_sort(a, left, right)
    # a[left] ~ a[right] 퀵정렬
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl+pr)//2, pr)
        x = a[m]
        # print(x)

        a[m], a[pr-1] = a[pr-1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x : pl += 1
            # print(a[pr])
            while a[pr] > x : pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        # print(left, pl, right, pr, a )
        if left < pr : qsort(a, left, pr)
        if pl < right : qsort(a, pl, right)
    return a

def quick_sort(a : MutableSequence) -> None:
    # 퀵 정렬
    qsort(a, 0, len(a)-1)
    return a

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    # print(lst)
    print(*quick_sort(lst), sep="\n")

