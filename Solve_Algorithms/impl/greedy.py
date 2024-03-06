# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution_greedy_1(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    lost.sort()
    lost_number = 0

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            lost_number += 1

    return n - lost_number

# print(solution_greedy_1(5, [2, 4], [1, 3, 5])) # 5