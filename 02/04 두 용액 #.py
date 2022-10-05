import sys
# sys.stdin = open('02\input.txt', 'r')

solution_num = int(sys.stdin.readline())
solution_list = list(map(int, sys.stdin.readline().split()))
solution_list=sorted(solution_list, key=abs)
# print(solution_list)

count = 3e9
result = []
for i in range(solution_num-1):
    temp = solution_list[i] + solution_list[i+1]
    # print(temp) #
    if abs(temp) < count:
        count = abs(temp)
        result = [solution_list[i], solution_list[i+1]]



# 같은 숫자!
# if abs(sum(result)) > abs(solution_list[0] + solution_list[0]):
#     result = [solution_list[0], solution_list[0]]

result.sort()
print(*result)
