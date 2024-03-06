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


# https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution_greedy_2(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer


# print(solution_greedy_2("JEROEN")) # 56