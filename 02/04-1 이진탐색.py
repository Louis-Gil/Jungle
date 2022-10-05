import sys
# sys.stdin = open('02\input.txt', 'r')

solution_num = int(sys.stdin.readline())
solution_list = sorted(list(map(int, sys.stdin.readline().split())))
# print(solution_num, solution_list)

start = 0
end = solution_num-1
minTake = sys.maxsize

while start < end:
    take = solution_list[start] + solution_list[end]
    if abs(take) < minTake:
        minTake = abs(take)
        result = [solution_list[start], solution_list[end]]
    if take < 0:
        start += 1
    elif take > 0:
        end -= 1
    else:
        break
print(result[0], result[1])