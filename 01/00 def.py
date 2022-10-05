from math import perm


def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

list1 = [1,2,3,4,5]
# for i in combinations_2(list1, 2):
#     print(i)
for i in permutations_2(list1, 2):
    print(i)
