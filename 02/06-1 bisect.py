import sys
from bisect import bisect_left

sys.stdin = open('02\input.txt', 'r')
input = sys.stdin.readline

sadae_num, animal_num, rifle =  map(int, sys.stdin.readline().split())
sadae_pos = sorted(list(map(int, input().split())))
animal_lst = [tuple(map(int, input().split())) for _ in range(animal_num)]
print(sadae_pos, animal_lst, rifle)


def findclosest_num(array, target):
    index = bisect_left(array, target)
    if index == 0:
        return array[index]
    if index == len(array):
        return array[-1]
    left = array[index-1]
    right = array[index]

    if target-left < right-target:
        return left
    return right

answer = 0

for x,y in animal_lst:
    closethunting_pos = findclosest_num(sadae_pos, x)

    if x - (rifle - y) <= closethunting_pos <= x + (rifle - y):
        answer += 1

print(answer)