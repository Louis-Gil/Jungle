# https://www.acmicpc.net/problem/2805
import sys
trees_num, needs = (map(int, sys.stdin.readline().split()))
trees_list = list(map(int, sys.stdin.readline().split()))
# print(trees_num, needs, trees_list)

def cut_tree(trees_list, needs, start, end):
    while start <= end:
        pin = (start + end)//2
        mount = 0
        for i in trees_list:
            if pin < i : mount += (i - pin)
        if mount >= needs:
            start = pin + 1
        else :
            end = pin - 1
    return end


start = 1
end = max(trees_list)
print(cut_tree(trees_list, needs, start, end))